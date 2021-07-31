import tkinter as tk

# Initiate and configure Top Level Wiget
window = tk.Tk()
window.title("Calculator")
window.geometry("270x270")

# Wiget Text
newText = tk.StringVar()

# Function for defining what happens when a button is pressed
def btnPressed(n):
    oldText = newText.get()
    nt = oldText + n
    if nt[-1] == "=":
        try:
            nt = nt[0:-1]
            nt = eval(nt)
        except:
            nt = "inf"
        finally:
            newText.set(nt)
    elif nt[-1] == "c":
        nt = oldText[0:-1]
        newText.set(nt)
    else:
        newText.set(nt)

# Function for defining Clear All
def clearAll():
    scrText = newText.get()
    scrText = ""
    newText.set(scrText)

# Textbox (parent window, text variable = StringVar, text is positioned if the widget has more space, border decor, bd = border size, fg = text color)
screen = tk.Label(window, textvariable = newText, anchor = "e", relief = "ridge", bd = 5, bg = "dark blue",fg = "white", font = ('arial', 12, 'bold'), width = 20)

# Widget: grid occupies 4 columns
screen.grid(row = 0, column = 0, columnspan = 4)

btnTup=("789/", "456*", "123+", "c0=-")
for i in btnTup:
    for j in range(4):
        tk.Button(window, text = i[j], height = 2, width = 5, command = lambda i = i, j = j: btnPressed(i[j])).grid(row = btnTup.index(i) + 1, column = j)

clearall = tk.Button(window, text = "Clear All", height=2, width=25, command = clearAll)
clearall.grid(row = 5, column = 0, columnspan = 4)

window.mainloop()
