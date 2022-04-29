from tkinter import *
from tkinter import font


window = Tk()
window.title("Calculator")
window.iconbitmap("plus_orange.ico")


frame = Frame(window)
frame.config(bg="#00ff00")
frame.pack()
e = Entry(frame, width=20, borderwidth=6, justify= "right",font="arial, 20")
e.grid(row=0, column=0,columnspan=4, padx=10, pady=10,sticky=W)


def button_click(number):
     current = e.get()
     e.delete(0, END)
     e.insert(0, str(current) + str(number))

def button_clear():
     e.delete(0, END)
     
def button_add():
     first_number = e.get()
     global f_num 
     global math   
     math = "plus"
     f_num = int(first_number)
     e.delete(0, END)

def button_divide():
     first_number = e.get()
     global f_num 
     global math   
     math = "divide"
     f_num = int(first_number)
     e.delete(0, END)
     
def button_multiple():
     first_number = e.get()
     global f_num 
     global math   
     math = "times"
     f_num = int(first_number)
     e.delete(0, END)

def button_subtract():
     first_number = e.get()
     global f_num 
     global math   
     math = "minus"
     f_num = int(first_number)
     e.delete(0, END)
     
def button_equal():
     second_number = e.get()
     e.delete(0, END)
     if math  == "plus":
          e.insert(0, f_num + int(second_number))
     
     if math == "divide":
          e.insert(0, f_num / int(second_number))
     
     if math == "times":
          e.insert(0, f_num * int(second_number))
        
     if math == "minus":
          e.insert(0, f_num - int(second_number))
     
     
     
btn1 = Button(frame, bg="#484C4E", fg="white", text=",", width=9, height=3, font="Arial, 12", command= lambda: button_click()).grid(row=5, column=0)
btn2 = Button(frame,  bg="#484C4E", fg="white", text="0", width=9, height=3, font="Arial, 12", command= lambda: button_click(0)).grid(row=5, column=1)
btn3 = Button(frame,  bg="#484C4E", fg="white", text="+", width=9, height=3, font="Arial, 12", command= button_add).grid(row=5, column=2)
btn4 = Button(frame,  bg="#484C4E", fg="white", text="1", width=9, height=3, font="Arial, 12", command= lambda: button_click(1)).grid(row=4, column=0)
btn5 = Button(frame,  bg="#484C4E", fg="white", text="2", width=9, height=3, font="Arial, 12", command= lambda: button_click(2)).grid(row=4, column=1)
btn6 = Button(frame,  bg="#484C4E", fg="white", text="3", width=9, height=3, font="Arial, 12", command= lambda: button_click(3)).grid(row=4, column=2)
btn7 = Button(frame,  bg="#484C4E", fg="white", text="4", width=9, height=3, font="Arial, 12", command= lambda: button_click(4)).grid(row=3, column=0)
btn8 = Button(frame, bg="#484C4E", fg="white", text="5", width=9, height=3, font="Arial, 12", command= lambda: button_click(5)).grid(row=3, column=1)
btn9 = Button(frame, bg="#484C4E", fg="white", text="6", width=9, height=3, font="Arial, 12", command= lambda: button_click(6)).grid(row=3, column=2)
btn10 = Button(frame, bg="#484C4E", fg="white", text="7", width=9, height=3, font="Arial, 12", command= lambda: button_click(7)).grid(row=2, column=0)
btn11 = Button(frame, bg="#484C4E", fg="white", text="8", width=9, height=3, font="Arial, 12", command= lambda: button_click(8)).grid(row=2, column=1)
btn12 = Button(frame, bg="#484C4E", fg="white", text="9", width=9, height=3, font="Arial, 12", command= lambda: button_click(9)).grid(row=2, column=2)

btn13 = Button(frame, bg="#777979", fg="white", text="DEL", width=9, height=3, font="Arial, 12", command= button_clear).grid(row=2, column=3)
btn14 = Button(frame, bg="#777979", fg="white", text="/", width=9, height=3, font="Arial, 12", command= button_divide).grid(row=3, column=3)
btn15 = Button(frame, bg="#777979", fg="white", text="x", width=9, height=3, font="Arial, 12", command= button_multiple).grid(row=4, column=3)
btn16 = Button(frame, bg="#777979", fg="white", text="-", width=9, height=3, font="Arial, 12", command= button_subtract).grid(row=5, column=3)

btn17 = Button(frame, text="=", width=9, height=3, font="Arial, 12", command= button_equal).grid(row=6, column=3, columnspan=2, sticky=E)

window.mainloop()