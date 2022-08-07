from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type", src="English",dest="Hindi"):

    text1 = text
    src1 = src
    dest1 = dest

    trans = Translator()
    trans1 = trans.translate(text, src= src1, dest= dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()

    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END,textget)



