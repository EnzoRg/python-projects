from tkinter import *


def draw_button(key, col, lin):
    boton = Button(window, text=key, command=lambda: press_button(key))
    boton.grid(column=col+1, row=lin+1)
    return boton


def press_button(key):
    if key == "C":
        disp["text"] = ""
    elif key == "←":
        disp["text"] = disp["text"][:-1]
    elif key == "=":
        disp["text"] = str(round(eval(disp["text"]), 6))
    else:
        disp["text"] += key


window = Tk()
window.title("Calculadora")
window.geometry("100x200")
window.resizable(width=True, height=True)

disp = Label(window, text="")
disp.grid(column=0, row=0, columnspan=5, sticky=W+E)

keys = "()C←789/456*123-.0=+"
buton_list = [draw_button(keys[n], n % 4, n//4) for n in range(20)]

window.mainloop()
