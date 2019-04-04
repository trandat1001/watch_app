import wx
from gui.WatchFrame import *

app = wx.App()
frame = WatchFrame(None)
frame.Show(True)
app.MainLoop()