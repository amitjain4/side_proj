##################################################################################
# Company: 
# Author: Jeffrey Lu
#
# Create Date: 05/03/2017
# Project Name: 
# Description: Python GUI for 
#
# Revision: 1
# Revision 1 - Initial Release
# 
##################################################################################
# -*- coding: utf-8 -*-
import platform
#import wxversion
#wxversion.select("3.0")
import wx, wx.html
import sys
import numpy as np

aboutText = """<p>This program is for ...
\nIt is running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>"""

# Check if Windows or Linus host 
(bits,linkage) = platform.architecture()
try:
    if(linkage.startswith('Windows')):
        if(bits == '32bit'):
            print '32bit has been detected'
        else:
            print '64bit has been detected'
    elif(linkage.startswith('ELF')):
        print 'Linux has been detected'
    else:
        print ''
except ImportError:
    print 'Unknown OS detected!'

class Panel1(wx.Panel):
    def __init__(self, parent, id=-1, size=wx.DefaultSize, color='BLUE'):
        wx.Panel.__init__(self, parent, id, wx.Point(0, 0), size, wx.SUNKEN_BORDER)
        self.WindowColor = color
        self.parent = parent

class Panel2(wx.Panel):
    def __init__(self, parent, id=-1, size=wx.DefaultSize, color='BLUE'):
        wx.Panel.__init__(self, parent, id, wx.Point(0, 0), size, wx.SUNKEN_BORDER)
        self.WindowColor = color
        self.parent = parent

class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About GUI program", style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())

class MyFrame(wx.Frame):
    def __init__(self, **kw):
        apply(wx.Frame.__init__, (self,), kw) # apply(function_name, arg list, kw dict)
        close_menu_on = 1;
        if(close_menu_on == 0):
            self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Create 'File' menu button
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")

        # Create 'About' menu button
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.SetMenuBar(menuBar)

        # Create status bar
        self.statusBar = self.CreateStatusBar()

        # Instantiate and configure RX OpalKelly card
        #self.xem1 = ok.FrontPanel()
        #self.fpga1 = fpga.Fpga_tx(self.xem1)

        # Create notebook
        self.nb = wx.Notebook(self, -1, style=wx.NB_TOP)
        self.nb.frame = self
        
        # Instantiate panels and add to notebook
        self.Panel1 = Panel1(parent=self.nb)
        self.Panel2 = Panel1(parent=self.nb)

        self.nb.AddPage(self.Panel1, "Panel 1")
        self.nb.AddPage(self.Panel2, "Panel 2")
        #self.nb.ChangeSelection(0)

        # sizer for notebook
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(self.nb, 1, wx.EXPAND) 
        self.SetAutoLayout(True)
        self.SetSizer(self.box)
        self.Layout()
        self.Center()

        # Required for the frame to show
        self.Show(True)

        # Timer instance for status bar 
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimerEvent, self.timer)
        self.timer.Start(milliseconds=5000, oneShot=False)

    def OnTimerEvent(self, event):
        self.statusBar.SetStatusText('Status bar text')

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()  

class App(wx.App):
    def OnInit(self):
        width = 1200;
        height = 900;
        frame = MyFrame(parent=None, id=-1, title='Title', pos=(0,0), size=(width, height))
        self.SetTopWindow(frame)
        return True

# Run the program
if __name__ == '__main__':
    app = App(0)
    app.MainLoop()