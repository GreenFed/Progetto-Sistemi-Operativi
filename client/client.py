from tkinter import filedialog
from tkinter import *
import os
from bitarray import bitarray
import serial

filename = ''
arduino = serial.Serial('/dev/ttyACM0', 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS)

def stopProg(e):
    root.destroy()

def open_file(e):
	global filename
	filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("txt files","*.txt"),("","*.*")))
	print(filename)

def send_file(e):
	arduino.reset_input_buffer()
	print(filename)
	f = open(filename, "rb")
	bit_array = bitarray()
	bit_array.fromfile(f)
	#bit_array.frombytes(b'Hello\n\n')
	#print(bit_array)
	s = stuffing(bit_array)
	print(s)
	f.close()
	print(bit_array.tobytes())
	#for b in bit_array.tobytes():
	print(arduino.write(s.tobytes()))
	#	print(chr(b))
		
	print("Finito di mandare")
	
	bit_array_risposta = bitarray()
	#print(arduino.in_waiting)
	
	while True:
		#print(arduino.in_waiting)
		c = arduino.read(1)
		if c == b'\x1b':
			break
		bit_array_risposta.frombytes(c)
		print(c)
			
	
	print(bit_array_risposta)
	print(len(bit_array_risposta))
	print(len(s))


def stuffing(ba):
	bit_array = bitarray('■')
	count = 0
	for b in ba:
		if b == 1:
			if count == 6:
				bit_array.extend('01')
				count = 1
			else:
				bit_array.extend('1')
				count = count + 1
		else:
			count = 0
			bit_array.extend('0')
			
	bit_array.extend('■')
	#print(bit_array)
	return bit_array

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
