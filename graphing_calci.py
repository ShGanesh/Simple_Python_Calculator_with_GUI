import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
import re

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]


def string2func(string): 							#evaluates the string and returns a function of x
    for word in re.findall('[a-zA-Z_]+', string):	# find all words and check if all are allowed:
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func


def printGraph(e):
	plt.clf()
	func = string2func(e)
	a = float(0)
	b = float(100)
	x = np.linspace(a, b, 250)

	plt.plot(x, func(x))
	plt.xlim(a, b)
	plt.show()


def printInput():
	ip=eqn.get()
	eqn.set=("")
	printGraph(ip) 


window=Tk()
eqn=tk.StringVar()
lbl=Label(window, text="Type your Equation", fg='red', font=("Helvetica", 16))
lbl.place(x=50, y=40)
lbl2=Label(window, text="y = ", fg='black', font=("Helvetica", 12))
lbl2.place(x=27, y=85)
txtfld=Entry(window, text="This is Entry Widget", textvariable=eqn, bd=6)
txtfld.place(x=60, y=80)
btn=Button(window, text="Plot", fg='blue', command=printInput)
btn.pack()
btn.place(x=120, y=120)

window.title('GRAPHING CALCULATOR')
window.geometry("300x180+10+10")
window.mainloop()


