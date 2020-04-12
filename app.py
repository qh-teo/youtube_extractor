from os import path
import logging
from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox, filedialog
from tkinter.ttk import *
from extractMP4 import download
window = Tk()

window.title("YouTube Downloader")
window.geometry("500x500")
window.resizable(width=False, height=False)


info_text = Label(window, text="To use, please click on button to download Youtube Videos:").grid(columnspan=2, sticky=W, padx=5)
Label(window, text="Enter link: ").grid(row=1, column=0, sticky=W,padx=5)

url_entry = Entry(window)
url_entry.focus()
url_entry.grid(row=1, column=0, sticky=E)

def clicked():
    if url_entry.get() == "":
        messagebox.showerror("Error", "No link was given. Please input a link for video to be extracted :)")
    else:
        dirname = filedialog.askdirectory(initialdir='/home/')
        download(dirname, url_entry.get())


btn = Button(window, text='Download', command=clicked)
btn.grid(column=0,row=3, sticky = W, padx=8, pady=5)



window.mainloop()
