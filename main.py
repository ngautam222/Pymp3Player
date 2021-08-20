from tkinter.filedialog import askdirectory
import tkinter
import pygame
import os
from tkinter.constants import SINGLE

player = tkinter.Tk()
player.title("Nicks player")
player.geometry("400x400")

dir = askdirectory()
os.chdir(dir)
songs = os.listdir()

lst = tkinter.Listbox(player,font="Helvetica",bg="white",selectmode=SINGLE)


player.mainloop()