from os import path
import logging
from tkinter import *
from tkinter import scrolledtext, filedialog, messagebox, filedialog
from tkinter.ttk import *
from extractMP4 import downloadMP4
from extractMP3 import downloadMP3
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
    elif video_music_selector.get() == "Select file format":
        messagebox.showerror("Error", "Please select which file format if you like to have your file saved as :)")
    else:
        dirname = filedialog.askdirectory(initialdir='/home/')
        if video_music_selector.get() == "MP4":  #extract MP4
            if sub_state.get() == 1:
                subtitles = True
            else:
                subtitles = False
            downloadMP4(dirname, url_entry.get(), subtitles)
            downloadmore()
        elif video_music_selector.get() == "MP3":  #extract MP3
            downloadMP3(dirname, url_entry.get())
            downloadmore()

def entry_checker():
    if url_entry.get() == "":
        messagebox.showerror("Error", "No link was given. Please input a link for video to be extracted :)")
    elif video_music_selector.get() == "Select file format":
        messagebox.showerror("Error", "Please select which file format if you like to have your file saved as :)")

def downloadmore():
    if messagebox.askyesno('Download Completed', 'Would you like to download another video?'):
        url_entry.delete()
    else:
        window.destroy()
#combobox codes
video_music_selector = Combobox(window)
video_music_selector['values'] = ("Select file format", "MP4", "MP3")
video_music_selector.current(0) #set the selected items
video_music_selector.grid(column=0, row=3, sticky=W, padx=8, pady=5)


sub_state = IntVar()
sub_state.set(1) #set check state
sub = Checkbutton(window, text='Subtitles', var=sub_state)
sub.grid(column=1, row=3, sticky=W)


btn = Button(window, text='Download!', command=clicked)
btn.grid(column=0,row=4, sticky=W, padx=8)



window.mainloop()
