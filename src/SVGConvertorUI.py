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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SVG Converter", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainSizer = wx.BoxSizer( wx.VERTICAL )

        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        PanelSizer = wx.BoxSizer( wx.VERTICAL )

        SVGSizer = wx.BoxSizer( wx.HORIZONTAL )

        SVGFileListChoices = []
        self.SVGFileList = wx.ListBox( self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SVGFileListChoices, wx.LB_MULTIPLE )
        SVGSizer.Add( self.SVGFileList, 1, wx.ALL|wx.EXPAND, 5 )

        ButtonSizer = wx.BoxSizer( wx.VERTICAL )

        self.AddFilesButton = wx.Button( self.MainPanel, wx.ID_ANY, u"添加文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.AddFilesButton, 0, wx.ALL, 5 )

        self.AddDirButton = wx.Button( self.MainPanel, wx.ID_ANY, u"添加目录", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.AddDirButton, 0, wx.ALL, 5 )

        self.RemoveButton = wx.Button( self.MainPanel, wx.ID_ANY, u"移除", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.RemoveButton, 0, wx.ALL, 5 )

        self.RemoveAllButton = wx.Button( self.MainPanel, wx.ID_ANY, u"移除全部", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.RemoveAllButton, 0, wx.ALL, 5 )


        ButtonSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.ExportButton = wx.Button( self.MainPanel, wx.ID_ANY, u"转换", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ExportButton.Enable( False )

        ButtonSizer.Add( self.ExportButton, 0, wx.ALL, 5 )


        SVGSizer.Add( ButtonSizer, 0, 0, 5 )


        PanelSizer.Add( SVGSizer, 0, wx.EXPAND, 5 )

        ExportTypeSizer = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"输出格式" ), wx.HORIZONTAL )

        self.ExportTypeLabel = wx.StaticText( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, u"输出格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ExportTypeLabel.Wrap( -1 )

        ExportTypeSizer.Add( self.ExportTypeLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        ExportTypeChoices = [ u"PDF", u"EPS" ]
        self.ExportType = wx.Choice( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ExportTypeChoices, 0 )
        self.ExportType.SetSelection( 0 )
        ExportTypeSizer.Add( self.ExportType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        ExportTypeSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.PDFVersionLabel = wx.StaticText( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, u"PDF 版本", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PDFVersionLabel.Wrap( -1 )

        ExportTypeSizer.Add( self.PDFVersionLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        PDFVersionChoices = [ u"PDF 1.5", u"PDF 1.4" ]
        self.PDFVersion = wx.Choice( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PDFVersionChoices, 0 )
        self.PDFVersion.SetSelection( 0 )
        ExportTypeSizer.Add( self.PDFVersion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        ExportTypeSizer.Add( ( 0, 0), 1, 0, 5 )

        self.EPSLevelLabel = wx.StaticText( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, u"EPS 级别", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.EPSLevelLabel.Wrap( -1 )

        ExportTypeSizer.Add( self.EPSLevelLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        EPSLevelChoices = [ u"PostScript 3", u"PostScript 2" ]
        self.EPSLevel = wx.Choice( ExportTypeSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, EPSLevelChoices, 0 )
        self.EPSLevel.SetSelection( 0 )
        self.EPSLevel.Enable( False )

        ExportTypeSizer.Add( self.EPSLevel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        PanelSizer.Add( ExportTypeSizer, 0, wx.EXPAND, 5 )

        ExportOptionSizer = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"输出选项" ), wx.VERTICAL )

        OptionSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.TextOptionLabel = wx.StaticText( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"文字选项", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TextOptionLabel.Wrap( -1 )

        OptionSizer.Add( self.TextOptionLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        TextOptionChoices = [ u"嵌入字体", u"转换为路径", u"输出为 LaTeX 文本" ]
        self.TextOption = wx.Choice( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, TextOptionChoices, 0 )
        self.TextOption.SetSelection( 1 )
        OptionSizer.Add( self.TextOption, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        OptionSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.ExportDPILabel = wx.StaticText( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出分辨率 (dpi)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ExportDPILabel.Wrap( -1 )

        OptionSizer.Add( self.ExportDPILabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ExportDPI = wx.TextCtrl( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"600", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        OptionSizer.Add( self.ExportDPI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        OptionSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.ExportSizeLabel = wx.StaticText( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出尺寸", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ExportSizeLabel.Wrap( -1 )

        OptionSizer.Add( self.ExportSizeLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        ExportSizeChoices = [ u"页面尺寸", u"对象尺寸" ]
        self.ExportSize = wx.Choice( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ExportSizeChoices, 0 )
        self.ExportSize.SetSelection( 1 )
        OptionSizer.Add( self.ExportSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        ExportOptionSizer.Add( OptionSizer, 1, wx.EXPAND, 5 )

        OutputSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.ExportDirLabel = wx.StaticText( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"输出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ExportDirLabel.Wrap( -1 )

        OutputSizer.Add( self.ExportDirLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ExportDir = wx.DirPickerCtrl( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
        OutputSizer.Add( self.ExportDir, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.SourceDirCheck = wx.CheckBox( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"原文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
        OutputSizer.Add( self.SourceDirCheck, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        ExportOptionSizer.Add( OutputSizer, 1, wx.EXPAND, 5 )

        InkscapeSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.InkscapeLable = wx.StaticText( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, u"Inkscape", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.InkscapeLable.Wrap( -1 )

        InkscapeSizer.Add( self.InkscapeLable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.InkscapeFile = wx.FilePickerCtrl( ExportOptionSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
        InkscapeSizer.Add( self.InkscapeFile, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        ExportOptionSizer.Add( InkscapeSizer, 1, wx.EXPAND, 5 )


        PanelSizer.Add( ExportOptionSizer, 0, wx.EXPAND, 5 )


        self.MainPanel.SetSizer( PanelSizer )
        self.MainPanel.Layout()
        PanelSizer.Fit( self.MainPanel )
        MainSizer.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( MainSizer )
        self.Layout()
        MainSizer.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.initMainFrame )
        self.AddFilesButton.Bind( wx.EVT_BUTTON, self.addFiles )
        self.AddDirButton.Bind( wx.EVT_BUTTON, self.addDirectory )
        self.RemoveButton.Bind( wx.EVT_BUTTON, self.removeFiles )
        self.RemoveAllButton.Bind( wx.EVT_BUTTON, self.removeAll )
        self.ExportButton.Bind( wx.EVT_BUTTON, self.export )
        self.ExportType.Bind( wx.EVT_CHOICE, self.toggleTypeVersion )
        self.SourceDirCheck.Bind( wx.EVT_CHECKBOX, self.toggleExportDirPicker )
        self.InkscapeFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.setInkscapeFile )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def initMainFrame( self, event ):
        event.Skip()

    def addFiles( self, event ):
        event.Skip()

    def addDirectory( self, event ):
        event.Skip()

    def removeFiles( self, event ):
        event.Skip()

    def removeAll( self, event ):
        event.Skip()

    def export( self, event ):
        event.Skip()

    def toggleTypeVersion( self, event ):
        event.Skip()

    def toggleExportDirPicker( self, event ):
        event.Skip()

    def setInkscapeFile( self, event ):
        event.Skip()


