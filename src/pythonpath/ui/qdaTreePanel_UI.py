# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Mon Jul  3 22:00:20 2017
#      by: unodit 0.7.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class qdaTreePanel_UI(unohelper.Base, XActionListener, XJobExecutor):

    """
    Class documentation...
    """
    def __init__(self, panelWin):
        
        self.LocalContext = uno.getComponentContext()
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        # self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        
        self.DialogContainer = panelWin
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)
        self.DialogModel.Moveable = True
        self.DialogModel.PositionY = "147"
        self.DialogModel.Height = 350
        self.DialogModel.PositionX = "176"
        self.DialogModel.Closeable = True
        self.DialogModel.Name = "Dialog1" #change back to tree dialog and see if it works
        self.DialogModel.Width = 163


        # --------- create an instance of Button control, set properties ---
        self.updateButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.updateButton.PositionY = "0"
        self.updateButton.Name = "updateButton"
        self.updateButton.TabIndex = 0
        self.updateButton.PositionX = "2"
        self.updateButton.Height = 16
        self.updateButton.Width = 60
        self.updateButton.Label = "Update"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("updateButton", self.updateButton)

        # add the action listener
        self.DialogContainer.getControl('updateButton').addActionListener(self)
        self.DialogContainer.getControl('updateButton').setActionCommand('updateButton_OnClick')

        self.textOfTag = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.textOfTag.Name = "textOfTag"
        self.textOfTag.PositionX = "2"
        self.textOfTag.Width = 140
        self.textOfTag.PositionY = "20"
        self.textOfTag.TabIndex = 1
        self.textOfTag.Height = 50
        self.textOfTag.MultiLine = True  #otherwise text won't be wrapped

        self.textOfTag.Text = "Click a tag below to display its corresponding source text here"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("textOfTag", self.textOfTag)

        # --------- create an instance of CheckBox control, set properties ---
        self.CheckboxJumpto = self.DialogModel.createInstance("com.sun.star.awt.UnoControlCheckBoxModel")

        self.CheckboxJumpto.Label = "Jump to clicked tag"
        self.CheckboxJumpto.Name = "CheckboxJumpto"
        self.CheckboxJumpto.PositionX = "64"
        self.CheckboxJumpto.PositionY = "2"
        self.CheckboxJumpto.Width = 74
        self.CheckboxJumpto.State = True
        self.CheckboxJumpto.TabIndex = 2
        self.CheckboxJumpto.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CheckboxJumpto", self.CheckboxJumpto)

        # --------- create an instance of .tree.TreeControl control, set properties ---
        self.TreeControl1 = self.DialogModel.createInstance("com.sun.star.awt.tree.TreeControlModel")
        
	# self.TreeControl1 = self.DialogModel.createInstance("com.sun.star.awt.tree.TreeControl")

        self.TreeControl1.PositionY = "80"
        self.TreeControl1.Name = "TreeControl1"
        self.TreeControl1.TabIndex = 2
        self.TreeControl1.PositionX = "2"
        self.TreeControl1.Height = 260
        self.TreeControl1.Width = 140

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TreeControl1", self.TreeControl1)

        #self.updateTree()
        


    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------
