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

from ui.Panel1_UI import Panel1_UI

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


class Panel1(Panel1_UI):
    '''
    Class documentation...
    '''
    def __init__(self, panelWin):
        Panel1_UI.__init__(self, panelWin)

        # document
        self.ctx = uno.getComponentContext()
        self.smgr = self.ctx.ServiceManager
        self.desktop = self.smgr.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)
        self.document = self.desktop.getCurrentComponent()

    def getHeight(self):
        return self.DialogContainer.Size.Height

    # --------- my code ---------------------
    # mri(self.LocalContext, self.DialogContainer)
    # xray(self.DialogContainer)

    def myFunction(self):
        # TODO: not implemented
        pass

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
        self.DialogContainer.execute()

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------


    def CommandButton1_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton1"
        self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
        # TODO: not implemented



def Run_Panel1(*args):
    """
    Intended to be used in a development environment only
    Copy this file in src dir and run with (Tools - Macros - MyMacros)
    After development copy this file back
    """
    ctx = uno.getComponentContext()
    sm = ctx.ServiceManager
    dialog = sm.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", ctx)

    app = Panel1(dialog)
    app.showDialog()

g_exportedScripts = Run_Panel1,
