# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrameUI
###########################################################################

class MainFrameUI ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SVG Converter", pos = wx.DefaultPosition, size = wx.Size( 811,546 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainSizer = wx.BoxSizer( wx.VERTICAL )

        SVGSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.SVGFileList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        SVGSizer.Add( self.SVGFileList, 0, wx.ALL, 5 )

        ButtonSizer = wx.BoxSizer( wx.VERTICAL )

        self.AddFilesButton = wx.Button( self, wx.ID_ANY, u"添加文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.AddFilesButton, 0, wx.ALL, 5 )

        self.AddDirButton = wx.Button( self, wx.ID_ANY, u"添加目录", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.AddDirButton, 0, wx.ALL, 5 )

        self.RemoveButton = wx.Button( self, wx.ID_ANY, u"移除", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.RemoveButton, 0, wx.ALL, 5 )

        self.RemoveAllButton = wx.Button( self, wx.ID_ANY, u"移除全部", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.RemoveAllButton, 0, wx.ALL, 5 )


        ButtonSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.ConvertButton = wx.Button( self, wx.ID_ANY, u"转换", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.ConvertButton, 0, wx.ALL, 5 )


        SVGSizer.Add( ButtonSizer, 1, wx.EXPAND, 5 )


        MainSizer.Add( SVGSizer, 1, wx.EXPAND, 5 )

        OutputFormatSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"输出格式" ), wx.HORIZONTAL )

        self.OutputFormatLabel = wx.StaticText( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, u"输出格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputFormatLabel.Wrap( -1 )

        OutputFormatSizer.Add( self.OutputFormatLabel, 0, wx.ALL, 5 )

        OutputFormatChoiceChoices = [ u"PDF", u"EPS" ]
        self.OutputFormatChoice = wx.Choice( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, OutputFormatChoiceChoices, 0 )
        self.OutputFormatChoice.SetSelection( 0 )
        OutputFormatSizer.Add( self.OutputFormatChoice, 0, wx.ALL, 5 )

        self.PDFVersionLabel = wx.StaticText( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, u"PDF 版本", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PDFVersionLabel.Wrap( -1 )

        OutputFormatSizer.Add( self.PDFVersionLabel, 0, wx.ALL, 5 )

        PDFVersionChoiceChoices = [ u"PDF 1.5", u"PDF 1.4" ]
        self.PDFVersionChoice = wx.Choice( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PDFVersionChoiceChoices, 0 )
        self.PDFVersionChoice.SetSelection( 0 )
        OutputFormatSizer.Add( self.PDFVersionChoice, 0, wx.ALL, 5 )

        self.EPSVersionLabel = wx.StaticText( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, u"EPS 版本", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.EPSVersionLabel.Wrap( -1 )

        OutputFormatSizer.Add( self.EPSVersionLabel, 0, wx.ALL, 5 )

        EPSVersionChoiceChoices = [ u"PostScript 3", u"PostScript 2" ]
        self.EPSVersionChoice = wx.Choice( OutputFormatSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, EPSVersionChoiceChoices, 0 )
        self.EPSVersionChoice.SetSelection( 0 )
        OutputFormatSizer.Add( self.EPSVersionChoice, 0, wx.ALL, 5 )


        MainSizer.Add( OutputFormatSizer, 1, wx.EXPAND, 5 )

        OutputOptionSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"输出选项" ), wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.TextOptionLabel = wx.StaticText( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"文字选项", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TextOptionLabel.Wrap( -1 )

        bSizer4.Add( self.TextOptionLabel, 0, wx.ALL, 5 )

        TextOptionChoiceChoices = [ u"嵌入字体", u"转换为路径", u"输出为 LaTeX 文本" ]
        self.TextOptionChoice = wx.Choice( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, TextOptionChoiceChoices, 0 )
        self.TextOptionChoice.SetSelection( 1 )
        bSizer4.Add( self.TextOptionChoice, 0, wx.ALL, 5 )

        self.OutputDPILabel = wx.StaticText( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出分辨率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputDPILabel.Wrap( -1 )

        bSizer4.Add( self.OutputDPILabel, 0, wx.ALL, 5 )

        self.OutputDPIText = wx.TextCtrl( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"600", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.OutputDPIText, 0, wx.ALL, 5 )

        self.OutputDPIUnitLabel = wx.StaticText( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"dpi", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputDPIUnitLabel.Wrap( -1 )

        bSizer4.Add( self.OutputDPIUnitLabel, 0, wx.ALL, 5 )

        self.OutputSizeLabel = wx.StaticText( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出尺寸", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputSizeLabel.Wrap( -1 )

        bSizer4.Add( self.OutputSizeLabel, 0, wx.ALL, 5 )

        OutputSizeChioceChoices = [ u"页面尺寸", u"对象尺寸" ]
        self.OutputSizeChioce = wx.Choice( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, OutputSizeChioceChoices, 0 )
        self.OutputSizeChioce.SetSelection( 1 )
        bSizer4.Add( self.OutputSizeChioce, 0, wx.ALL, 5 )


        OutputOptionSizer.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.OutputDirLabel = wx.StaticText( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.OutputDirLabel.Wrap( -1 )

        bSizer5.Add( self.OutputDirLabel, 0, wx.ALL, 5 )

        self.OutputDirPicker = wx.DirPickerCtrl( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"选择文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer5.Add( self.OutputDirPicker, 0, wx.ALL, 5 )

        self.SourceDirCheck = wx.CheckBox( OutputOptionSizer.GetStaticBox(), wx.ID_ANY, u"原文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.SourceDirCheck, 0, wx.ALL, 5 )


        OutputOptionSizer.Add( bSizer5, 1, wx.EXPAND, 5 )


        MainSizer.Add( OutputOptionSizer, 1, wx.EXPAND, 5 )


        self.SetSizer( MainSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.AddFilesButton.Bind( wx.EVT_BUTTON, self.addFiles )
        self.AddDirButton.Bind( wx.EVT_BUTTON, self.addDirectory )
        self.RemoveButton.Bind( wx.EVT_BUTTON, self.removeFiles )
        self.RemoveAllButton.Bind( wx.EVT_BUTTON, self.removeAll )
        self.ConvertButton.Bind( wx.EVT_BUTTON, self.convert )
        self.OutputFormatChoice.Bind( wx.EVT_CHOICE, self.toggleFormatVersion )
        self.SourceDirCheck.Bind( wx.EVT_CHECKBOX, self.disableOutputDirPicker )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def addFiles( self, event ):
        event.Skip()

    def addDirectory( self, event ):
        event.Skip()

    def removeFiles( self, event ):
        event.Skip()

    def removeAll( self, event ):
        event.Skip()

    def convert( self, event ):
        event.Skip()

    def toggleFormatVersion( self, event ):
        event.Skip()

    def disableOutputDirPicker( self, event ):
        event.Skip()


