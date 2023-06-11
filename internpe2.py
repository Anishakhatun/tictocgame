from tkinter import*
from tkinter.ttk import*

#importing
from time import strftime

root = Tk()
root.title("DIGITAL CLOCK")

#this function is used to display time on the label
def clock():
    Time_str = strftime('%H:%M:%S:%P')
    Time.config(Text = Time_str)
    Time.after(1000,clock)

#style the label
Time = Label(root,font = ("ds-digital",80),background = "black",foreground = "lime")

#placing clock at the center
Time.pack(anchor_=_"center")
clock()
mainloop()
    
