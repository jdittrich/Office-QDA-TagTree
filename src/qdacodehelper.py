# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Write your code here
#
# =============================================================================

import uno
import unohelper

from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX

from com.sun.star.ui import XUIElementFactory
from com.sun.star.lang import XComponent
from com.sun.star.ui import XUIElement, XToolPanel,XSidebarPanel, LayoutSize
from com.sun.star.frame import XDispatch,XDispatchProvider
from com.sun.star.ui.UIElementType import TOOLPANEL as UET_TOOLPANEL

from ui_logic.qdaTreePanel import qdaTreePanel

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

def messageBox(MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
    ctx = uno.getComponentContext()
    sm = ctx.ServiceManager
    si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", ctx)
    toolkit = sm.createInstanceWithContext("com.sun.star.awt.ExtToolkit", ctx)
    mBox = si.createMessageBox(toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
    mBox.execute()


class ElementFactory( unohelper.Base, XUIElementFactory):
    """
    UNO service that implements the com/sun/star/ui/XUIElementFactory interface.
    If you write a new factory then add it to Factories.xcu
    Method createUIElement(URL,arguments) is called for URLs defined in Sidebar.xcu.
    """

    def __init__(self, ctx):
        self.ctx = ctx

    def createUIElement(self, url, args):

        try:
            xParentWindow = None
            xFrame = None
            xUIElement = None

            for arg in args:
                if arg.Name == "Frame":
                    xFrame = arg.Value
                elif arg.Name == "ParentWindow":
                    xParentWindow = arg.Value

            xUIElement = XUIPanel(self.ctx, xFrame, xParentWindow, url)

            # getting the real panel window
            # for setting the content
            xUIElement.getRealInterface()
            panelWin = xUIElement.Window

            # panelWin has to be set visible
            panelWin.Visible = True

            # get and set height to receive a working scrollbar
            height = showPanels(panelWin, url)
            xUIElement.height = height

            return xUIElement

        except Exception as e:
            print(e)
            tb()

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
        ElementFactory,
        "tagtree.qdaaddon.de.fordes.qdatreehelper",
        ("com.sun.star.task.Job",),)


class XUIPanel( unohelper.Base,  XSidebarPanel, XUIElement, XToolPanel, XComponent):

    def __init__(self, ctx, frame, xParentWindow, url):

        self.ctx = ctx
        self.xParentWindow = xParentWindow
        self.window = None
        self.height = 100

    # XUIElement
    def getRealInterface(self):

        
        if not self.window:
            dialogUrl = "vnd.sun.star.extension://tagtree.qdaaddon.de.fordes.qdatreehelper/empty_dialog.xdl"
            smgr = self.ctx.ServiceManager

            provider = smgr.createInstanceWithContext("com.sun.star.awt.ContainerWindowProvider", self.ctx)
            self.window = provider.createContainerWindow(dialogUrl, "", self.xParentWindow, None)

        return self

    @property
    def Frame(self):
        self.frame = frame

    @property
    def ResourceURL(self):
        return self.name

    @property
    def Type(self):
        return UET_TOOLPANEL

    # XComponent
    def dispose(self):
        pass

    def addEventListener(self, ev): pass

    def removeEventListener(self, ev): pass

    # XToolPanel
    def createAccessible(self, parent):
        return self

    @property
    def Window(self):
        return self.window

    # XSidebarPanel
    def getHeightForWidth(self, width):
        # print("getHeightForWidth: %s" % width)
        # return LayoutSize(0, -1, 0) # full height
        return LayoutSize(self.height, self.height, self.height)

    # LO5.1-
    def getMinimalWidth(self):
        return 50

class test(unohelper.Base, XDispatch, XDispatchProvider):

    IMPLE_NAME = "tagtree.qdaaddon.de.fordes.ProtocolHandler"
    SERVICE_NAMES = IMPLE_NAME,

    @classmethod
    def get_imple(klass):
        #pydevBrk()
        return klass, klass.IMPLE_NAME, klass.SERVICE_NAMES

    def __init__(self, *args):
        pass

    def queryDispatches(self, *args):
        return

    def queryDispatch(self, featureURL, frameName, searchFlag):
        return self

    def dispatch(self, featureURL, args):
        self.showDefaultMenuCommand(featureURL)

    def addStatusListener(self, listener, featureURL):
        #print('addStatusListener', featureURL.Path)
        return

    def removeStatusListener(self, listener, featureURL):
        #print('removeStatusListener', featureURL.Path)
        return

    def showDefaultMenuCommand(self, featureURL):
        """
        Command that is dispatched when the user clicks on
        the "More Options" button in the panel title bar
        """

        if featureURL.Path == 'qdaTreePanel':
            #TODO minor: put message into central object instead of code
            messageBox("Helper for qualitative Research in LibreOffice. Generates a list/tree of #hashtags#subhashtags in comments which can serve as codes and/or markers for memos", 'DefaultMenuCommand', MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK)
            # messageBox(featureURL.Path, 'DefaultMenuCommand', MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK)



g_ImplementationHelper.addImplementation(*test.get_imple())


def showPanels(panelWin, url):
    """
    Create a new panel object when the sidebar is initialized
    or whenever a panel becomes visible
    """
    
    ctx = uno.getComponentContext()
    # url is set in Sidebar.xcu
    if url == 'private:resource/toolpanel/qdatreehelper/qdaTreePanel':
        
        pos_y = 20

        app = qdaTreePanel(panelWin)
        app.showDialog()
        panel_height = app.getHeight()

        return panel_height + pos_y

