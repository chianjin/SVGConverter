"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import sys
import os.path
import wx
import SVGConvertorMainFrame


# Implementing MainFrame
class SVGConvertor(SVGConvertorMainFrame.MainFrame):
    def __init__(self, parent):
        SVGConvertorMainFrame.MainFrame.__init__(self, parent)
        self.svg_files = []
        self.SVGFileList.InsertColumn(0, '文件名')
        self.SVGFileList.InsertColumn(1, '文件路径')

    # Handlers for MainFrame events.
    def addFiles(self, event):
        # TODO: Implement addFiles
        with wx.FileDialog(self, "添加 SVG 文件", wildcard="SVG files (*.svg)|*.svg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            self.svg_files.extend(fileDialog.GetPaths())
            for f in self.svg_files:
                filename = os.path.basename(f)
                dirname = os.path.dirname(f)
                index = self.SVGFileList.InsertItem(65535, filename)
                self.SVGFileList.SetItem(index, 1, dirname)
                print(index)


    def addDirectory(self, event):
        # TODO: Implement addDirectory
        pass

    def removeFiles(self, event):
        # TODO: Implement removeFiles
        pass

    def removeAll(self, event):
        # TODO: Implement removeAll
        pass

    def convert(self, event):
        # TODO: Implement convert
        pass

    def toggleFormatVersion(self, event):
        # TODO: Implement toggleFormatVersion
        pass

    def disableOutputDirPicker(self, event):
        # TODO: Implement disableOutputDirPicker
        pass