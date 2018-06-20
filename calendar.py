from tkinter import *
import datetime
import calendar
yy=datetime.date.today().year
mm=datetime.date.today().month
root = Tk()
text = Text(root)
text.insert(INSERT, calendar.month(yy, mm))
text.insert(END, " ")
text.pack()
text.tag_add("here", "1.0", "2.0")
text.tag_add("start", "2.0", "3.0")
text.tag_add("fart", "3.0", "8.0")
text.tag_config("here", background = "red", foreground = "black")
text.tag_config("start", background = "yellow", foreground = "black")
text.tag_config("fart", background = "green", foreground = "black")
root.mainloop()
