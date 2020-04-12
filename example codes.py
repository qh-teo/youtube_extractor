# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)
# txt = Entry(window, text="Hello")
# txt.grid(column=1, row=0)
# txt.focus()

#combobox codes
# combo = Combobox(window)
# combo['values']=(1,2,3,4,5,"Text")
# combo.current(1) #set the selected items
# combo.grid(column=0, row=0)

# checkbox codes
# chk_state = BooleanVar()
# chk_state.set(True) #set check state
# chk = Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=0)

# selected = IntVar()
#
# # Radiobvtton
# rad1=Radiobutton(window,text='First', value=1, variable=selected)
# rad2=Radiobutton(window,text='Second', value=2, variable=selected)
# red3=Radiobutton(window,text='Third', value=3, variable=selected)
#
# def clicked():
#     print(selected.get())
#
#
# btn = Button(window, text="Click Me", command=clicked)
#
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# red3.grid(column=2, row=0)
# btn.grid(column=3, row=0)


# button codes
# def clicked():
#     res = "Welcome to " + txt.get()
#     lbl.configure(text=res)
#
#
# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=2, row=0)

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showerror("Error", "No link was added in")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()