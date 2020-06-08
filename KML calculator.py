
# we will create a calculator using tkinter 

        # importing all from tkinter

from tkinter import *

root = Tk()
root.title("KML calculator")


#                we create a text zone where the numbers and the result will show
zone = Entry(root, width=9, font=("Courier", 45), borderwidth=0)


#                here we create all the functions that we will need in our program

#     click function for insert every number in the text zone
def click(number):
    if number == ".":
        button_p["state"]=DISABLED
    now = zone.get()
    zone.delete(0, END)    
    zone.insert(0, str(now) + str(number))



#     delet function for delete the last index in the text zone
def delet():
    last = zone.get()
    if last[-1] == ".":
        button_p["state"] = ACTIVE
    last = last[0: len(last)-1]
    zone.delete(0, END)
    zone.insert(0, last)

#      sub function define the subtraction
def sub():
    button_p["state"] = ACTIVE
    global first_num
    global opperation
    first_num = zone.get()
    opperation = "sub"
    zone.delete(0 , END)

#      mult function define the multiplication
def mult():
    button_p["state"] = ACTIVE
    global first_num
    global opperation
    first_num = zone.get()
    opperation = "mult"
    zone.delete(0 , END)

#      div function define the division
def div():
    button_p["state"] = ACTIVE
    global first_num
    global opperation
    first_num = zone.get()
    opperation = "div"
    zone.delete(0 , END)

#      add function define the addition
def add():
    button_p["state"] = ACTIVE
    global first_num
    global opperation
    first_num = zone.get()
    opperation = "add"
    zone.delete(0 , END)

#      clear function for clean the board from all  previous values 
def clear():
    button_p["state"] = ACTIVE
    zone.delete(0, END)
    last_num = 0.0
    first_num = 0.0

#      global_result function insert the result of the operations in the text zone
def global_result():
    button_p["state"] = ACTIVE
    global last_num
    last_num = zone.get()
    zone.delete(0, END)
    if opperation == "add":
        zone.insert(0, float(first_num) + float(last_num))
    elif opperation == "div":
        zone.insert(0, float(first_num) / float(last_num))
    elif opperation == "mult":
        zone.insert(0, float(first_num) * float(last_num))
    elif opperation == "sub":
        zone.insert(0, float(first_num) - float(last_num))




#                            creating all the buttons of the calculator

#         this first button just for clean the board from empty places
button_vide= Button(root, text=" ", width=46, height=26, bg="#2e86de", borderwidth=0, state=DISABLED)
button_vide.grid(row=1, column=0, columnspan=4, rowspan=6)



#   values buttons
button_1 = Button(root, text="1" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(1))
button_2 = Button(root, text="2" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(2))
button_3 = Button(root, text="3" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(3))
button_4 = Button(root, text="4" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(4))
button_5 = Button(root, text="5" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(5))
button_6 = Button(root, text="6" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(6))
button_7 = Button(root, text="7" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(7))
button_8 = Button(root, text="8" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(8))
button_9 = Button(root, text="9" , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(9))
button_0 = Button(root, text="0" , width=6, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click(0))
button_p = Button(root, text="." , width=3, bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 25), command=lambda: click("."))

#     operations buttons
button_div = Button(root, text="/"   , width=3, bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30),command=div)
button_mult = Button(root, text="*"  , width=3, bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30),command=mult)
button_sub = Button(root, text="-"   , width=3, bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30),command=sub)
button_add = Button(root, text="+"   , width=3, bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30),command=add)

#       calculator functions buttons
button_del = Button(root, text="Del" , width=3, bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30), command=delet)
button_equal = Button(root, text="="   , width=10,  bg="#48dbfb", fg="#ee5253", borderwidth=0, font=("Courier", 30),command=global_result)
button_clear = Button(root, text="clear"   , width=20,  bg="#2e86de", fg="white", borderwidth=0, font=("Courier", 20),command=clear)



#                     showing all the buttons on the sceen


#         row 0
zone.grid(row=0, column=0, columnspan=4)



#         row 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_del.grid(row=1, column=3)


#         row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_div.grid(row=2, column=3)


#         row 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mult.grid(row=3, column=3)


#         row 4
button_0.grid(row=4, column=0, columnspan=2)
button_p.grid(row=4, column=2,)
button_sub.grid(row=4, column=3)


#          row 5
button_equal.grid(row=5, column=0, columnspan=3)
button_add.grid(row=5, column=3)


#          row6
button_clear.grid(row=6, column=0, columnspan=4)


#     lunch the program
root.mainloop()