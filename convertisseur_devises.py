import tkinter as tk
from tkinter import ttk
from tkinter import *

USD = 1.25
EUR = 1.17
RUP = 83.87
PES = 25.68

label = tk.Label()
label.grid()


fenetre = Tk()
fenetre.title("Convertisseur monney")
fenetre.config(bg = "#87CEEB")

l = Label(fenetre, text = "montant à convertir")
e = Entry(fenetre)
d = Label(fenetre, text = "devise d'entrée")

# crétion de la liste des élément du combobox
monnaies = ["USD, EUR, RUP, PES"]
# création de l'ojet combobox

listeCombo = ttk.combobox(root, values = monnaies)
listeCombo.current(1)
listeCombo.bind("<<ComboboxSelected>>", action)
listeCombo.pack()

s = Label(fenetre, text = "devise de sortie")

devises = ["USD, EUR, RUP, PES"]
# création de l'ojet combobox

listeCombo = ttk.combobox(root, values = monnaies)
listeCombo.current(1)
listeCombo.bind("<<ComboboxSelected>>", action)
listeCombo.pack()

l.pack()
e.pack()
d.pack()
s.pack


def clear():
    label.config(text="")
    
tk.Button(text="clear", command=clear).grid()


fenetre.mainloop()

def action(event):
    select = listeCombo.get
    if select == USD:
        select * Entry

    if select == EUR:
        select * Entry

    if select == RUP:
        select * Entry

    if select == PES:
        select * Entry


