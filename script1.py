from tkinter import *

window=Tk()
window.geometry("500x200")
window.title("Weight Conversion")

def from_kg():
    grams=float(el_value.get())*1000
    pound=float(el_value.get())*2.2
    ounce=float(el_value.get())*35.3

    t1.delete('1.0', END)
    t1.insert(END, grams)
    t2.delete('1.0', END)
    t2.insert(END, pound)
    t3.delete('1.0', END)
    t3.insert(END, ounce)    

el_value = StringVar() 
e1 = Label(window, text = "Enter the weight in Kg", font = ('calibre',10,'normal')) 
e2 = Entry(window, textvariable = el_value, bg = "light cyan", font = ('calibre',10,'normal')) 
e3 = Label(window, text = 'Gram', font = ('calibre',10,'normal')) 
e4 = Label(window, text = 'Pounds', font = ('calibre',10,'normal')) 
e5 = Label(window, text = 'Ounce', font = ('calibre',10,'normal'))      

t1 = Text(window, height = 1, width = 20, bg = "light cyan") 
t2 = Text(window, height = 1, width = 20, bg = "light cyan") 
t3 = Text(window, height = 1, width = 20, bg = "light cyan") 

b1=Button(window, text="Calculate", command=from_kg)

e1.grid(row = 0, column = 0) 
e2.grid(row = 0, column = 1) 
e3.grid(row = 1, column = 0) 
e4.grid(row = 1, column = 1) 
e5.grid(row = 1, column = 2) 
t1.grid(row = 2, column = 0) 
t2.grid(row = 2, column = 1) 
t3.grid(row = 2, column = 2) 
b1.grid(row = 0, column = 2) 

window.mainloop()