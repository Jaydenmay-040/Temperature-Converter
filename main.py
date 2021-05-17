from tkinter import *
from tkinter.messagebox import showerror


# The info for the window
window = Tk()
window.title("Temperature Converter")
window.geometry("620x620")
window.resizable(False, False)


def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    result = (f - 32) * 5/9
    G_entry.insert(0, round(result, 2))


def celsius_to_fahrenheit(c):
    result = c*9/5+32
    G_entry.insert(0, round(result, 2))


# activates the one and disables the other
def activate_f_to_c():
    F_entry.config(state=NORMAL)
    C_entry.config(state=DISABLED)
    global fahrenheit_to_celsius
    fahrenheit_to_celsius = "Fahrenheit"


# activates the one and disables the other
def activate_c_to_f():
    C_entry.config(state=NORMAL)
    F_entry.config(state=DISABLED)
    global fahrenheit_to_celsius
    fahrenheit_to_celsius = "Celsius"


def clear_results():
    G_entry.delete(0, END)


def conversion():
    global fahrenheit_to_celsius
    if fahrenheit_to_celsius == "Fahrenheit":
        if test_if_float(float(F_entry.get())):
            fahrenheit_to_celsius(float(F_entry.get()))
        else:
            messagebox.showinfo("Error", " Enter a number")
    elif fahrenheit_to_celsius == "Celsius":
        print(type(F_entry.get()))

        if test_if_float(float(C_entry.get())):

            celsius_to_fahrenheit(float(C_entry.get()))
        else:
            messagebox.showinfo("Error", " Enter a number")


def test_if_float(f):
    if type(f) == float:
        return True
    else:
        return False


# The info that is displayed in the window(The Fahrenheit symbol and entry)
F_frame = LabelFrame(window, text="Fahrenheit -- Celsius", width=205, height=125)
F_frame.place(x=80, y=70)
F_entry = Entry(F_frame, width=15, state=DISABLED)
F_entry.place(x=20, y=60)
F_btn = Button(window, text="Activate - Fahrenheit to Celsius", command=activate_f_to_c)
F_btn.place(x=70, y=200)

# The info that is displayed in the window(The Celsius symbol and entry)
C_frame = LabelFrame(window, text="Celsius -- Fahrenheit ", width=205, height=125)
C_frame.place(x=350, y=70)
C_entry = Entry(C_frame, width=15, state=DISABLED)
C_entry.place(x=20, y=60)
C_btn = Button(window, text="Activate - Celsius to Fahrenheit", command=activate_c_to_f)
C_btn.place(x=340, y=200)

# Close program, Calculate conversion and clear buttons
# Also the green entry.
G_entry = Entry(window, bg="#7CFC00", width=25)
G_entry.place(x=250, y=300)


def delete():
    F_entry.delete(0, 'end')
    C_entry.delete(0, 'end')
    G_entry.config(state="normal")
    G_entry.delete(0, END)
    G_entry.config(state="readonly")


btn2 = Button(window, text="Calculate the conversion", command=conversion)
btn2.place(x=50, y=300)
clear = Button(window, text="Clear", width=15, command=delete).place(x=500, y=300)
quite = Button(window, text="Close Program", width=15, command="exit").place(x=470, y=350)

window.mainloop()
