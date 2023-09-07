from tkinter import ttk
from tkinter import *
import pandas as pd
import tkinter as tk


prog = tk.Tk()
prog.config(width=500, height=500)
prog.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=["1", "2"]
)
meniu = Menu(prog)
prog.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
auk = 1
#df = pd.read_csv('data1.csv')
#print(df)

def Aukstas():

    auk = combo.get()
    if auk == '1':
        auk = ('data1.csv')
    elif auk == '2':
        auk = ('data2.csv')
    print (auk)
    return auk

auk = Aukstas()







def Darb():

    Darbuotojas = Toplevel(prog)
    Darbuotojas.title("Darbuotojai")
    Darbuotojas.geometry("200x200")
    Label(Darbuotojas,
          text="Darbuotojai").pack()
    meniu = Menu(Darbuotojas)
    Darbuotojas.config(menu=meniu)
    submeniu = Menu(meniu, tearoff=0)
    meniu.add_cascade(label="Meniu", menu=submeniu)
    submeniu.add_command(label="Atsijungti")
    submeniu.add_command(label="Iseiti",
                         command=Darbuotojas.destroy)
    df = pd.read_csv('data1.csv')
    print(df)
    scrollbaras = Scrollbar(Darbuotojas)
    boksas = Listbox(Darbuotojas)
    scrollbaras.config(command=boksas.yview)
    boksas.insert(END, *df)
    scrollbaras.pack(side=RIGHT, fill=Y)
    boksas.pack(side=LEFT)


def Stal():

    Staliukas = Toplevel(prog)
    Staliukas.title("Staliukai")
    Staliukas.geometry("200x200")
    Label(Staliukas,
          text="Staliukai").pack()
    meniu = Menu(Staliukas)
    Staliukas.config(menu=meniu)
    submeniu = Menu(meniu, tearoff=0)
    meniu.add_cascade(label="Meniu", menu=submeniu)
    submeniu.add_command(label="Atsijungti")
    submeniu.add_command(label="Iseiti",
                         command=Staliukas.destroy)
    #masyvas2 = range(1, 21)
    #df = pd.read_csv("data1.csv", usecols="Staliukai")
    df = pd.read_csv('data1.csv')
    print (df)
    scrollbaras = Scrollbar(Staliukas)
    boksas = Listbox(Staliukas)
    scrollbaras.config(command=boksas.yview)
    boksas.insert(END, *df)
    scrollbaras.pack(side=RIGHT, fill=Y)
    boksas.pack(side=LEFT)

def Laim():

    Laimejimai = Toplevel(prog)
    Laimejimai.title("Laimejimai")
    Laimejimai.geometry("200x200")
    Label(Laimejimai,
          text="Laimejimai").pack()
    meniu = Menu(Laimejimai)
    Laimejimai.config(menu=meniu)
    submeniu = Menu(meniu, tearoff=0)
    meniu.add_cascade(label="Meniu", menu=submeniu)
    submeniu.add_command(label="Atsijungti")
    submeniu.add_command(label="Iseiti",
                         command=Laimejimai.destroy)
    #masyvas2 = range(1, 21)
    #df = pd.read_csv("data1.csv", usecols="Staliukai")
    df = pd.read_csv('data1.csv')
    print (df)
    scrollbaras = Scrollbar(Laimejimai)
    boksas = Listbox(Laimejimai)
    scrollbaras.config(command=boksas.yview)
    boksas.insert(END, *df)
    scrollbaras.pack(side=RIGHT, fill=Y)
    boksas.pack(side=LEFT)


virsutinis = Frame(prog)
apatinis = Frame(prog)

mygtukas1 = Button(virsutinis, text="Darbuotojas", command = Darb)
mygtukas2 = Button(virsutinis, text="Staliukas", command = Stal)
mygtukas3 = Button(virsutinis, text="Laimejimai", command = Laim)
mygtukas4 = Button(apatinis, text="Pasirinkti auksta", command =Aukstas)



virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Atsijungti")
submeniu.add_command(label="Iseiti",
command=prog.destroy)
combo.pack(side=BOTTOM)
















prog.mainloop()
