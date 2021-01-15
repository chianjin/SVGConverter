#
#

import wx
from SVGConvertor import SVGConvertor

if __name__ == '__main__':
    app =wx.App()
    form = SVGConvertor(None)
    form.Show()
    app.MainLoop()
