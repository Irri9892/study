import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('タイトル')
        self.SetBackgroundColour((200, 200, 200))
        self.SetPosition((200, 100))
        self.SetSize((400, 500))
        self.Show()

        panel_disp = wx.Panel(self, -1, pos = (10, 10), size = (365, 75))
        panel_disp.SetBackgroundColour((0, 255, 0))

        panel_button = wx.Panel(self, -1)
        panel_button.SetBackgroundColour((0, 0, 255))
        panel_button.SetPosition((10, 100))
        panel_button.SetSize((365, 350))

        label_disp = wx.StaticText(panel_disp, -1, "sd",)
        label_disp.SetFont(wx.Font(40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        label_disp.SetLabel("a")

        button_7 = wx.Button(panel_button, -1, "7")
        button_8 = wx.Button(panel_button, -1, "8")
        button_9 = wx.Button(panel_button, -1, "9")
        button_divid = wx.Button(panel_button, -1, "/")
        button_4 = wx.Button(panel_button, -1, "4")
        button_5 = wx.Button(panel_button, -1, "5")
        button_6 = wx.Button(panel_button, -1, "6")
        button_multiply = wx.Button(panel_button, -1, "*")
        button_1 = wx.Button(panel_button, -1, "1")
        button_2 = wx.Button(panel_button, -1, "2")
        button_3 = wx.Button(panel_button, -1, "3")
        button_minus = wx.Button(panel_button, -1, "-")
        button_0 = wx.Button(panel_button, -1, "0")
        button_dot = wx.Button(panel_button, -1, ".")
        button_equal = wx.Button(panel_button, -1, "=")
        button_plus = wx.Button(panel_button, -1, "+")

        layout = wx.GridSizer(rows=4, cols=4, gap=(0, 0))
        layout.Add(button_7)
        layout.Add(button_8)
        layout.Add(button_9)
        layout.Add(button_divid)
        layout.Add(button_4)
        layout.Add(button_5)
        layout.Add(button_6)
        layout.Add(button_multiply)
        layout.Add(button_1)
        layout.Add(button_2)
        layout.Add(button_3)
        layout.Add(button_minus)
        layout.Add(button_0)
        layout.Add(button_dot)
        layout.Add(button_equal)
        layout.Add(button_

        panel_button.SetSizer(layout)




app = wx.App()
MyApp(None)
app.MainLoop()