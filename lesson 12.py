from tkinter import Tk, Frame, TOP, StringVar, Entry, RIGHT, Button

windows = Tk()
width = windows.winfo_screenwidth()
height = windows.winfo_screenheight()
center_x = int(width / 2 - 240 / 2)
center_y = int(height / 2 - 320 / 2)
windows.geometry(f"{240}x{320}+{center_x}+{center_y}")
windows.configure(bg="black")

input_frame = Frame(windows,
                    width=240, height=50,
                    highlightbackground="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

text = StringVar()
entry = Entry(input_frame,
              font=("Calibri", 15, "bold"),
              textvariable=text,
              justify=RIGHT,
              bg="black", fg="white")
entry.grid(row=0, column=0, ipady=14, ipadx=17)

counter = ""  # global


def clear_button():
    global counter
    counter = ""
    text.set("")


def equal_button():
    global counter
    result = eval(counter)
    text.set(result)
    counter = ""


def click_button(item):
    global counter
    counter += item
    text.set(counter)


buttons_frame = Frame(windows, width=312,
                      height=274, bg="grey")
buttons_frame.pack()

bolish_bosilgan = 0
qoshish_bosilgan = 0
ayirish_bosilgan = 0
kopaytirish_bosilgan = 0
daraja_bosilgan = 0
foiz_bosilgan = 0

# firth row
clear = Button(buttons_frame, text="AC", width=5,
               command=lambda: clear_button(), bg="grey", fg="white", font=("calibri", 15, "bold"))
clear.grid(row=0, column=0, ipady=5, )

daraja = Button(buttons_frame, text="a**2", width=5,
                command=lambda: click_button("**"), bg="grey", fg="white", font=("calibri", 15, "bold"))
daraja.grid(row=0, column=1, ipady=5, )

foiz = Button(buttons_frame, text="%", width=5,
              command=lambda: click_button("%"), bg="grey", fg="white", font=("calibri", 15, "bold"))
foiz.grid(row=0, column=2, ipady=5, )

divide = Button(buttons_frame, text="/", width=5,
                command=lambda: click_button("/"), bg="orange", fg="white", font=("calibri", 15, "bold"))
divide.grid(row=0, column=3, ipady=5)

# second row
seven = Button(buttons_frame, text="7", width=5,
               command=lambda: click_button("7"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
seven.grid(row=1, column=0, ipady=5)

eight = Button(buttons_frame, text="8", width=5,
               command=lambda: click_button("8"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
eight.grid(row=1, column=1, ipady=5)

nine = Button(buttons_frame, text="9", width=5,
              command=lambda: click_button("9"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
nine.grid(row=1, column=2, ipady=5)

multiple = Button(buttons_frame, text="*", width=5,
                  command=lambda: click_button("*"), bg="orange", fg="white", font=("calibri", 15, "bold"))
multiple.grid(row=1, column=3, ipady=5)

# 3 row
four = Button(buttons_frame, text="4", width=5,
              command=lambda: click_button("4"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
four.grid(row=2, column=0, ipady=5)

five = Button(buttons_frame, text="5", width=5,
              command=lambda: click_button("5"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
five.grid(row=2, column=1, ipady=5)

six = Button(buttons_frame, text="6", width=5,
             command=lambda: click_button("6"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
six.grid(row=2, column=2, ipady=5)

minus = Button(buttons_frame, text="-", width=5,
               command=lambda: click_button("-"), bg="orange", fg="white", font=("calibri", 15, "bold"))
minus.grid(row=2, column=3, ipady=5)

# 4 row
three = Button(buttons_frame, text="3", width=5,
               command=lambda: click_button("3"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
three.grid(row=3, column=2, ipady=5)

two = Button(buttons_frame, text="2", width=5,
             command=lambda: click_button("2"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
two.grid(row=3, column=1, ipady=5)

one = Button(buttons_frame, text="1", width=5,
             command=lambda: click_button("1"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
one.grid(row=3, column=0, ipady=5)

add = Button(buttons_frame, text="+", width=5,
             command=lambda: click_button("+"), bg="orange", fg="white", font=("calibri", 15, "bold"))
add.grid(row=3, column=3, ipady=5)

# 5 row
zero = Button(buttons_frame, text="0", width=11,
              command=lambda: click_button("0"), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
zero.grid(row=4, column=0, ipady=5, columnspan=2)

dot = Button(buttons_frame, text=".", width=5,
             command=lambda: click_button("."), bg="darkgrey", fg="white", font=("calibri", 15, "bold"))
dot.grid(row=4, column=2, ipady=5)

equal = Button(buttons_frame, text="=", width=5,
               command=lambda: equal_button(), bg="orange", fg="white", font=("calibri", 15, "bold"))
equal.grid(row=4, column=3, ipady=5)

windows.mainloop()
