from tkinter import *
import datetime
import calendar
yy=datetime.date.today().year
mm=datetime.date.today().month
dd=datetime.date.today().day

root = Tk()
text = Text(root)
text.insert(INSERT, calendar.month(yy, mm))
text.insert(END, "El día de hoy es: " + str(dd))
text.pack()
text.tag_add("here", "1.0", "2.0")
text.tag_add("start", "2.0", "3.0")
text.tag_add("fart", "3.0", "8.0")
text.tag_config("here", background = "skyblue", foreground = "black")
text.tag_config("start", background = "black", foreground = "white")
text.tag_config("fart", background = "white", foreground = "black")
root.mainloop()
 
