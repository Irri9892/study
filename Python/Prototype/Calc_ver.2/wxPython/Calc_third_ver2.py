import wx


class CalcFrame(wx.Frame):

    def __init__(self):

        super().__init__(None, wx.ID_ANY, "Calc", size=(300, 230))

        root_panel = wx.Panel(self, -1)

        text_panel = TextPanel(root_panel)
        cmdbutton_panel = CommandButtonPanel(root_panel)
        calcbutton_panel = CalcButtonPanel(root_panel)

        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(text_panel, 0, wx.GROW | wx.ALL, border = 10)
        root_layout.Add(cmdbutton_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border = 20)
        root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)

class TextPanel(wx.Panel):

    def __init__(self, parent):

        super().__init__(parent, -1)

        calc_text = wx.TextCtrl(self, -1, style = wx.TE_RIGHT)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)

class CommandButtonPanel(wx.Panel):

    def __init__(self, parent):

        super().__init__(parent, -1)

        button_ce = wx.Button(self, -1, "CE")
        button_c = wx.Button(self, -1, "C")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_ce, flag = wx.GROW)
        layout.Add(button_c, flag = wx.GROW)
        self.SetSizer(layout)

class CalcButtonPanel(wx.Panel):

    def __init__(self, parent):

        super().__init__(parent, -1)

        button_collection = ('7', '8', '9', '+',
                             '4', '5', '6', '-',
                             '1', '2', '3', '*',
                             '0', '.', '=', '/')

        layout = wx.GridSizer(4, 4, 3, 3)

        for i in button_collection:
            layout.Add(wx.Button(self, -1, i, size = (30, 25)), 1, wx.GROW)

        self.SetSizer(layout)


application = wx.App()
frame = CalcFrame()
frame.Show()
application.MainLoop()