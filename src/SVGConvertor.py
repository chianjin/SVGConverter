"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import os
# import sys
import subprocess
from glob import glob
from tempfile import mkstemp
import wx
import SVGConvertorUI

from pprint import pprint


# Implementing MainFrame
class SVGConvertor(SVGConvertorUI.MainFrameUI):
    def __init__(self, parent):
        SVGConvertorUI.MainFrameUI.__init__(self, parent)
        self.svg_files = []
        self.inkscape_file = ''
        self.export_options = []
        self.export_folder = ''
        self.export_type = 'pdf'
        self.export_to_source_folder = False

        self.searchInkscapeFile()

    # Handlers for MainFrameUI events.
    def initMainFrame(self, event):
        pass

    def addFiles(self, event):
        # addFiles
        with wx.FileDialog(self, "添加 SVG 文件", wildcard="SVG files (*.svg)|*.svg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_OK:
                self.addToFileList(fileDialog.GetPaths())
                self.toggleExportButton()

    def addFolder(self, event):
        # TODO: Implement addDirectory
        with wx.DirDialog(self, '添加包含 SVG 文件的目录',
                          style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_OK:
                self.addToFileList(glob('{0}/*.svg'.format(dirDialog.GetPath())))
                self.toggleExportButton()

    def removeFiles(self, event):
        # removeFiles
        selections = self.SVGFileList.GetSelections()
        if selections:
            selections.reverse()
            for index in selections:
                self.SVGFileList.Delete(index)
                self.svg_files.pop(index)
            self.toggleExportButton()

    def removeAll(self, event):
        # removeAll
        self.SVGFileList.Clear()
        self.toggleExportButton()

    def export(self, event):
        self.exportFiles()
        if not self.export_to_source_folder:
            self.moveExportedFiles()

    def exit(self, event):
        pass

    def setExportType( self, event ):
        index = self.ExportType.GetSelection()
        export_type = self.ExportType.GetString(index)
        self.export_type = export_type.lower()
        if export_type == 'PDF':
            self.PDFVersion.Enable()
            self.EPSLevel.Disable()
        elif export_type == 'EPS':
            self.PDFVersion.Disable()
            self.EPSLevel.Enable()

    def setExportFolder(self, event):
        with wx.DirDialog(self, '添加包含 SVG 文件的目录',
                          style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_OK:
                self.export_folder = dirDialog.GetPath()
                self.ExportFolder.SetValue(self.export_folder)
                self.toggleExportButton()

    def setExportToSourceFolder(self, event):
        self.export_to_source_folder = self.ExportToSourceFolderCheck.IsChecked()
        self.ExportFolder.Enable(not self.export_to_source_folder)
        self.ExportFolderButton.Enable(not self.export_to_source_folder)
        if self.export_to_source_folder:
            self.export_folder = ''
        else:
            self.export_folder = self.ExportFolder.GetValue()
        self.toggleExportButton()

    def setInkscapeFile(self, event):
        with wx.FileDialog(self, "选择 Inkscape 程序", wildcard="Inkscape 程序|inkscape.com",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_OK:
                self.inkscape_file = fileDialog.GetPath()
                self.InkscapeFile.SetValue(self.inkscape_file)
                self.toggleExportButton()

    # Functions in main
    def toggleExportButton(self):
        export_ok = self.inkscape_file and self.svg_files
        export_ok = export_ok and (self.export_to_source_folder or self.export_folder)
        self.ExportButton.Enable(bool(export_ok))

    def addToFileList(self, files):
        for file in files:
            if file not in self.svg_files:
                self.SVGFileList.Append(file)
                self.svg_files.append(file)

    def searchInkscapeFile(self):
        inkscape_cmd = r'inkscape\bin\inkscape.com'
        paths = [os.environ['ProgramFiles'], os.environ['ProgramFiles(x86)']]
        paths.extend(os.environ['PATH'].split(';'))
        for path in paths:
            inkscape_file = os.path.join(path, inkscape_cmd)
            if os.path.exists(inkscape_file):
                self.inkscape_file = inkscape_file
                self.InkscapeFile.SetValue(self.inkscape_file)

    def setExportOptions(self):
        # Export Format
        index = self.ExportType.GetSelection()
        self.export_options.append('--export-type={0}'.format(self.export_type))

        # Export PDF version or EPS level
        if self.export_type == 'pdf':
            index = self.PDFVersion.GetSelection()
            pdf_version = self.PDFVersion.GetString(index).split()[-1]
            self.export_options.append('--export-pdf-version={0}'.format(pdf_version))
        elif self.export_type == 'eps':
            index = self.EPSLevel.GetSelection()
            ps_level = self.EPSLevel.GetString(index).split()[-1]
            self.export_options.append('--export-ps-level={0}'.format(ps_level))

        # Text export option
        index = self.TextOption.GetSelection()
        if index == 1:
            self.export_options.append('--export-text-to-path')
        elif index == 2:
            self.export_options.append('--export-latex')

        # Export DPI
        dpi = self.ExportDPI.GetValue()
        self.export_options.append('--export-dpi={0}'.format(dpi))

        # Export size
        index = self.ExportSize.GetSelection()
        if index == 0:
            self.export_options.append('--export-area-page')
        elif index == 1:
            self.export_options.append('--export-area-drawing')
            
    def exportFiles(self):
        self.export_options = []
        self.setExportOptions()
        export_cmd = [self.inkscape_file]
        export_cmd.extend(self.export_options)
        export_cmd.extend(self.svg_files)
        try:
            self.ExportButton.Disable()
            p = subprocess.run(export_cmd)
        except subprocess.CalledProcessError:
            dialog = wx.MessageBox(self, '发生错误，请检查', '错误', style=wx.OK | wx.ICON_ERROR )
            dialog.ShowModal()
            dialog.Destroy()
        finally:
            self.ExportButton.Enable()

    def moveExportedFiles(self):
        for file in self.svg_files:
            dirname, filename = os.path.split(file)
            if dirname != self.export_folder:
                filename, ext = os.path.splitext(filename)
                filename = '{0}.{1}'.format(filename, self.export_type)
                source_file = os.path.join(dirname, filename)
                dist_file = os.path.join(self.export_folder, filename)
                os.replace(source_file, dist_file)
