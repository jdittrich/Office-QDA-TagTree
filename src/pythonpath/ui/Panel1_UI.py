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


class Panel1_UI(unohelper.Base, XActionListener, XJobExecutor):
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
        self.DialogContainer = panelWin
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)
        self.DialogModel.Name = "Dialog2"
        self.DialogModel.PositionX = "202"
        self.DialogModel.Moveable = True
        self.DialogModel.Closeable = True
        self.DialogModel.PositionY = "60"
        self.DialogModel.Height = 369
        self.DialogModel.Width = 138


        # --------- create an instance of Edit control, set properties ---
        self.TextField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField1.TabIndex = 1
        self.TextField1.PositionX = "2"
        self.TextField1.Name = "TextField1"
        self.TextField1.PositionY = "156"
        self.TextField1.Height = 178
        self.TextField1.Width = 133

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField1", self.TextField1)

        # --------- create an instance of .tree.TreeControl control, set properties ---
        self.TreeTags = self.DialogModel.createInstance("com.sun.star.awt.tree.TreeControlModel")

        self.TreeTags.TabIndex = 0
        self.TreeTags.PositionY = "5"
        self.TreeTags.Name = "TreeTags"
        self.TreeTags.PositionX = "1"
        self.TreeTags.Height = 130
        self.TreeTags.Width = 134

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TreeTags", self.TreeTags)

        # --------- create an instance of CheckBox control, set properties ---
        self.CheckboxJumpto = self.DialogModel.createInstance("com.sun.star.awt.UnoControlCheckBoxModel")

        self.CheckboxJumpto.State = False
        self.CheckboxJumpto.TabIndex = 2
        self.CheckboxJumpto.PositionX = "60"
        self.CheckboxJumpto.Name = "CheckboxJumpto"
        self.CheckboxJumpto.Label = "Jump to clicked tag"
        self.CheckboxJumpto.PositionY = "344"
        self.CheckboxJumpto.Height = 12
        self.CheckboxJumpto.Width = 74

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CheckboxJumpto", self.CheckboxJumpto)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.TabIndex = 3
        self.CommandButton1.PositionY = "342"
        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.Label = "CommandButton1"
        self.CommandButton1.PositionX = "5"
        self.CommandButton1.Height = 20
        self.CommandButton1.Width = 54

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------