
import tkinter as tk
import requests
from tkinter import *
#from PIL import Image, ImageTK
# positional commands object.pack()
# object.grid()
# object.
#could not complete the app as something went wrong with the API code  - it was not activated for the first 30 minutes 
def test_function(entry):
	print("Button Clicked!", entry)

def get_weather(city):
	print(city)


def translate(DNA):

 import re
 genetic_code={
 'AAA':'K',
 'AAG':'K',
 'AAC':'N',
 'AAU':'N',
 'AGA':'R',
 'AGG':'R',
 'AGC':'S',
 'AGU':'S',
 'ACA':'T',
 'ACG':'T',
 'ACC':'T',
 'ACU':'T',
 'AUA':'I',
 'AUG':'M',
 'AUC':'I',
 'AUU':'I',
 'GAA':'E',
 'GAG':'E',
 'GAC':'D',
 'GAU':'D',
 'GGA':'G',
 'GGG':'G',
 'GGC':'G',
 'GGU':'G',
 'GCA':'A',
 'GCG':'A',
 'GCC':'A',
 'GCU':'A',
 'GUA':'V',
 'GUG':'V',
 'GUC':'V',
 'GUU':'V',
 'CAA':'Q',
 'CAG':'Q',
 'CAC':'H',
 'CAU':'H',
 'CGA':'R',
 'CGG':'R',
 'CGC':'R',
 'CGU':'R',
 'CCA':'P',
 'CCG':'P',
 'CCC':'P',
 'CCU':'P',
 'CUA':'L',
 'CUG':'L',
 'CUC':'L',
 'CUU':'L',
 'UAA':'*',
 'UAG':'*',
 'UAC':'Y',
 'UAU':'Y',
 'UGA':'*',
 'UGG':'W',
 'UGC':'C',
 'UGU':'C',
 'UCA':'S',
 'UCG':'S',
 'UCC':'S',
 'UCU':'S',
 'UUA':'L',
 'UUG':'L',
 'UUC':'F',
 'UUU':'F'              }
 protein_codon_list=re.findall('...',DNA) #moves in 3s and finds all letters 
 protein=''
 for i in protein_codon_list:
#protein.append(genetic_code[i])
  protein+=genetic_code[i]
 print(protein)
 label['text'] = protein

 
def vape(bazz):
	print(bazz)


root = tk.Tk()
HEIGHT=700
WIDTH=800

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image =tk.PhotoImage(file='dna.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#cc66ff', bd=5) # bd=5 gives boarders to the frame 
frame.place(relx=0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, )
entry.place(relwidth=0.65, relheight=1)
#need a lambda function
button = tk.Button(frame, text="I love Iris", font=40, command=lambda: translate(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame=tk.Frame(root, bg='#cc66ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, wraplength=1000)
label.place(relwidth=1, relheight=1)



root.mainloop()

