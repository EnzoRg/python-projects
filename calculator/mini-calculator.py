from tkinter import *


def boton_dibujar(key, col, lin):
    boton = Button(window, text=key, command=lambda: boton_press(key))
    boton.grid(column=col+1, row=lin+1)
    return boton


def boton_press(key):
    if key == "C":
        disp["text"] = ""
    elif key == "<":
        disp["text"] = disp["text"][:-1]
    elif key == "=":
        disp["text"] = str(round(eval(disp["text"]), 6))
    else:
        disp["text"] += key


window = Tk()
window.title("Calculadora")

disp = Label(window, text="")
disp.grid(column=0, row=0, columnspan=5)

keys = "()C<789/456*123-.0=+"
buton_list = [boton_dibujar(keys[n], n % 4, n//4) for n in range(20)]

window.mainloop()
