# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Write your code here
#
# =============================================================================

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX

from com.sun.star.awt import XActionListener

from com.sun.star.view import XSelectionChangeListener
from com.sun.star.view import XSelectionSupplier
from com.sun.star.view.SelectionType import SINGLE

from functools import reduce

import re

from ui.qdaTreePanel_UI import qdaTreePanel_UI

# ----------------- helpers for API_inspector tools -----------------

# uncomment for MRI
#def mri(ctx, target):
#    mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
#    mri.inspect(target)

# uncomment for Xray
#from com.sun.star.uno import RuntimeException as _rtex
#def xray(myObject):
#    try:
#        sm = uno.getComponentContext().ServiceManager
#        mspf = sm.createInstanceWithContext("com.sun.star.script.provider.MasterScriptProviderFactory", uno.getComponentContext())
#        scriptPro = mspf.createScriptProvider("")
#        xScript = scriptPro.getScript("vnd.sun.star.script:XrayTool._Main.Xray?language=Basic&location=application")
#        xScript.invoke((myObject,), (), ())
#        return
#    except:
#        raise _rtex("\nBasic library Xray is not installed", uno.getComponentContext())


class qdaTreePanel(qdaTreePanel_UI,XActionListener, XSelectionChangeListener):
    '''
    Class documentation...
    '''
    
    def __init__(self, panelWin):
        qdaTreePanel_UI.__init__(self, panelWin)

        # document
        self.ctx = uno.getComponentContext()
        self.smgr = self.ctx.ServiceManager
        self.desktop = self.smgr.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)
        self.document = self.desktop.getCurrentComponent()
        self.updateTree() # this, seemingly, does not work

    def getHeight(self):
        return self.DialogContainer.Size.Height

    # --------- my code ---------------------
    # mri(self.LocalContext, self.DialogContainer)
    # xray(self.DialogContainer)

    def updateTree(self): #why is self implicitly passed?
        def convertAbstractToUiTree(abstractTree,parent,gui_treemodel):
            print(abstractTree)
            if not abstractTree: #if abstract tree is empty, show some into to the user
                branch = treemodel.createNode("if you create comments write a #hashtag, they will be listed here", False)
                parent.appendChild(branch)
                
            for item in abstractTree: #TODO: Item is sometimes the string "children"
                
                if "children" in item and item["children"]:
                    branch = treemodel.createNode("#"+item['name'], True) #[:n] takes the first n chars of a string (or just leaves it be, if there are less). Alternatives: if-clause or function for it; gain: add "…" to string if shortened 
                else:
                    branch = treemodel.createNode(item['name'][:20], False) 
               
                if "children" in item and item["children"]: #"in" checks for keys existance, "item["children"]"" checks if list is emptry since an empty list is false (https://www.python.org/dev/peps/pep-0008/#programming-recommendations)
                    convertAbstractToUiTree(item["children"],branch, gui_treemodel)
                    
                if "data" in item:
                    branch.DataValue = item["data"]["origAnnotation"]
                parent.appendChild(branch)

        
        document = self.document

        treeControl = self.DialogContainer.getControl('TreeControl1')
        commentslist = collectHashtaggedComments(document)
        abstractTree = constructTree(commentslist)
        sortTreeRecursive(abstractTree) #inplace sort

        treemodel = self.ServiceManager.createInstance("com.sun.star.awt.tree.MutableTreeDataModel")

        rootnode = treemodel.createNode("root",True)
        treemodel.setRoot(rootnode)

        convertAbstractToUiTree(abstractTree, rootnode, treemodel)

        # so seemingly, the dialog is created just via models. To get the views/controlers we need to call the getControl.
        # To add to the irritation, there is the tree model (model of the control element) and the tree data model (model of what the control element shows)
        treeControl.addSelectionChangeListener(self)
        
        self.TreeControl1.DataModel = treemodel
        
        toolkit = self.ServiceManager.createInstance("com.sun.star.awt.Toolkit")
        
        treeControl.createPeer(toolkit,None)
        
        expandAllNodesGuiTree(treeControl.Model.DataModel.Root, treeControl)

        # the variable single has been imported by "from com.sun.star.view.SelectionType import SINGLE". Just "SINGLE" (as string) or the corrseponding enumeration number did not work.
        self.TreeControl1.SelectionType = SINGLE
        self.TreeControl1.RootDisplayed = False

        expandAllNodesGuiTree(treeControl.Model.DataModel.Root, treeControl)
    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.LocalContext.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.LocalContext)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        self.updateTree() # can now execute the update (and within expand the nodes) since the peer is set now, and this is needed for expanding nodes (whyever...)
        self.DialogContainer.execute()

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------


    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'updateButton_OnClick':
            self.updateButton_OnClick()

    def updateButton_OnClick(self):
        self.updateTree()
#         self.DialogModel.Title = "It's Alive! - updateButton"
#         self.messageBox("It's Alive! - updateButton", "Event: OnClick", INFOBOX)
        
    def selectionChanged(self, ev):
        selection = ev.Source.getSelection().DataValue #get id of item
        self.selection = selection
        self.textOfTag.Text = selection.getAnchor().getString()
        #mri(self.LocalContext, XSCRIPTCONTEXT.getDocument())
        
        if self.CheckboxJumpto.State == True:
            scrollToRange(self.document, selection.getAnchor())


#--------------------------------------------

def scrollToRange(document, range): #range is a section in a text

    #DOES: scrolls the document to the range in a given text
    #ARGUMENTS: a document and a range object. The range must be in the document
    #RETURNS: nothing (is a side effect function, see DOES)
    
    viewCursor = document.CurrentController.getViewCursor()
    viewCursor.gotoRange(range,False)
    viewCursor.collapseToEnd() #if not collapsed, the whole range is marked and is easily accidental overwritten with an accidental keystroke

def collectHashtaggedComments(document):
    
    # DOES: Collect all comments ("Annotations") that match a regex in an array
    # GETs: A document
    # RETURNs: List of comments ("Annotations")

    findHashtagsRegex = re.compile('#\S+') #This regex needs to match for a comment to be included in the returned list. It is: a "#", followed by any non-whitespace, followed by word boundary

    textfields = document.getTextFields()

    matchedComments = [] #will hold array with comments and their metadata
    counter=0;#counter for providing a locally unique id

    for currentField in textfields:
            if currentField.supportsService("com.sun.star.text.TextField.Annotation"): #is this an annotation aka comment?

                #to list/array
                #write to var
                if findHashtagsRegex.search(currentField.Content): # only do, if a hashtag is in the comment
                    tagListStrings = findHashtagsRegex.findall(currentField.Content) #the tags in the comment field
                    markedText = currentField.getAnchor().getString() # the text to which the comment refers
                    tagList =[] #to be filled with the split strings (=list of strings) from tagListStrings

                    for string in tagListStrings: #TODO: there is probably a more elegant way
                        tagList.append(string[1:].split("#")) #remove first character. If the first character would be a # it would create an empty string when split in this place

                    annotationInfo =    {
                                        'name':markedText,
                                        'paths':tagList,
                                        'data':{
                                            'id':counter,
                                            'origAnnotation':currentField,
                                            'markedText':markedText,
                                            'content':currentField.Content,
                                            }
                                        } # create hashtable with infos to use late

                    counter = counter +1; # this probably could be done better.

                    # jumpt to da point
                    matchedComments.append(annotationInfo)
    return matchedComments

def constructTree(commentsArray):
    '''
    DOES: Create a nested tree from a flat list 
    GETs: A list with items having name (string), paths (list of paths each being a list composed of path parts), data (a dict with what you like – it’s payload)
    RETURNS: a tree like this
    
    - A
     * Children:
      - B
       * children:
        - D
        - E
      - C
    …
    So it is lists of dicts. One property is "children", in which there is another list of dicts etc.
    '''
    
    #TODO: Fix "array" name to "list"  
    
    result = []

    initialValue = {
        0:result
    }

    for comment in commentsArray:
        for path in comment["paths"]:
            #pydevd.settrace()
            def reducerfunction(accumulator,pathpart): #function defined here so I can access the current comment in the reducer function
                #print("cmmt", comment, "-- -- - -path",path, "- - - pathpart", pathpart)
                if not pathpart in accumulator:
                    accumulator[pathpart] = {
                        0:[]
                    }

                    elementToAppend = {
                        "name":pathpart,
                        "children":accumulator[pathpart][0]
                    }

                    if pathpart == comment["name"] and "data" in comment:
                        elementToAppend["data"] = comment["data"]

                    accumulator[0].append(elementToAppend)
                return accumulator[pathpart]

            reduce(reducerfunction,path+[comment["name"]],initialValue)

    return result



def sortTreeRecursive(treeList):
    ''' 
    DOES: Sort children lists in a tree by name
    GET: Tree
    RETURN: Nothing, side effect
    '''
    for item in treeList:
        if "children" in item:
            sortTreeRecursive(item["children"])
    treeList.sort(key=lambda item:item["name"])
    
def expandAllNodesGuiTree(root,treeControl):
    '''
    DOES: Expand all Nodes in a mutableTreeModel
    GETS: XTreeNode
    RETURNS: Nothing, side effect
    '''

    # TODO: check if tree control has a peer, if not return None
    for count in range(0,root.ChildCount):
        child = root.getChildAt(count)
        
        if child.ChildCount > 0:
            treeControl.expandNode(child)
            expandAllNodesGuiTree(child, treeControl)

        
    
    


#----------------#
#-- RUN PANEL----#
#----------------#

def Run_qdaTreePanel(*args):
    """
    Intended to be used in a development environment only
    Copy this file in src dir and run with (Tools - Macros - MyMacros)
    After development copy this file back
    """
    ctx = uno.getComponentContext()
    sm = ctx.ServiceManager
    dialog = sm.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", ctx)

    app = qdaTreePanel(dialog)
    app.showDialog()

g_exportedScripts = Run_qdaTreePanel,
