from tkinter import filedialog
from tkinter import *
import os
from bitarray import bitarray

filename = ''

def stopProg(e):
    root.destroy()

def open_file(e):
	global filename
	filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

def send_file(e):
	print(filename)
	f = open(filename, "rb")
	bit_array = bitarray()
	bit_array.fromfile(f)
	print(bit_array)
	f.close()

root=Tk()
root.title("Progetto Sistemi Operativi")

frame = Frame(root, width=960, height=540)

status_text = Label(frame, text="Status: Not connected")
status_text.pack()

open_filedialog=Button(frame, text="Open file")
open_filedialog.pack()
open_filedialog.bind('<Button-1>',open_file)

send_button=Button(frame, text="Send file")
send_button.pack()
send_button.bind('<Button-1>',send_file)

frame.pack()

root.mainloop()
