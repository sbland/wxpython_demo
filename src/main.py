import wx
from wx import xrc


class MyApp(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource('app.xrc')
        self.init_frame()
        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'mainFrame')
        self.panel = xrc.XRCCTRL(self.frame, 'mainPanel')
        self.button = xrc.XRCCTRL(self.panel, 'button')
        self.frame.Bind(wx.EVT_BUTTON, self.OnNewFrame, self.button)
        self.frame.Show()

    def OnNewFrame(self, evt):
        self.frame2 = self.res.LoadFrame(None, 'nextFrame')
        self.frame2.Show()


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()