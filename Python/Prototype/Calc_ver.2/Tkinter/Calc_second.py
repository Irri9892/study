import tkinter as tk

win = tk.Tk()
win.title("Calc") # タイトル
win.geometry("400x100") # サイズ

label = tk.Label(win, text = "式を入力")
label.pack()

text = tk.Entry(win, width = 50)
text.pack
text.place(x = 50, y = 30)

var = tk.StringVar()

label2 = tk.Label(win, textvariable = var)
label2.pack()
label2.place(x = 210, y = 65)



def ok_click():
    strings = str(eval(text.get()))
    var.set(strings)

okButton = tk.Button(win, text = "=", command=ok_click)
okButton.pack()
okButton.place(x = 185, y = 60)

win.mainloop()