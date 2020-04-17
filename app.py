from tkinter import *
from tkinter import scrolledtext, messagebox, filedialog, ttk
from tkinter.ttk import *
from extractMP4 import download_mp4
from extractMP3 import download_mp3


class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.title("YouTube Downloader")
        self.geometry("350x175")
        self.resizable(width=False, height=False)

        info_text = Label(self, text="To use, please click button to download Youtube Videos:", font=("Helvetica", 10)).grid(columnspan=2,
            padx=5)
        Label(self, text="Enter link: ").grid(row=1, column=0, sticky=W, padx=5)

        url_entry = Entry(self)
        url_entry.focus()
        url_entry.grid(row=1, column=0, sticky=E)

        # combobox codes
        video_music_selector = Combobox(self)
        video_music_selector['values'] = ("Select file format", "MP4", "MP3")
        video_music_selector.current(0)  # set the selected items
        video_music_selector.grid(column=0, row=3, sticky=W, padx=8, pady=5)

        sub_state = IntVar()
        sub_state.set(1)  # set check state
        sub = Checkbutton(self, text='Subtitles', var=sub_state)
        sub.grid(column=1, row=3, sticky=W)

        download_notify = Label(self, text="Downloading....")

        def clicked():
            if url_entry.get() == "":
                messagebox.showerror("Error", "No link was given. Please input a link for video to be extracted :)")

            elif video_music_selector.get() == "Select file format":
                messagebox.showerror("Error",
                                     "Please select which file format if you like to have your file saved as :)")

            else:
                dirname = filedialog.askdirectory(title='Choose A Save Location', initialdir='/home/')
                download_notify.grid(column=0, row=5, sticky=W, padx=8)

                if video_music_selector.get() == "MP4":  # extract MP4
                    if sub_state.get() == 1:
                        subtitles = True
                    else:
                        subtitles = False
                    download_mp4(dirname, url_entry.get(), subtitles)
                    download_notify.configure(text="Downloaded!")
                    download_more()

                elif video_music_selector.get() == "MP3":  # extract MP3
                    download_mp3(dirname, url_entry.get())
                    download_notify.configure(text="Downloaded!")
                    download_more()

        def download_more():  # prompts user if they will want to download more videos
            if messagebox.askyesno('Download Completed', 'Would you like to download another video?'):
                url_length = len(url_entry.get())
                print(url_length)
                url_entry.delete(first=0, last=url_length)
                download_notify.grid_forget()
            else:
                self.destroy()

        btn = Button(self, text='Download!', command=clicked)
        btn.grid(column=0, row=4, sticky=W, padx=8)



if __name__ == '__main__':
    app = Gui()
    app.mainloop()
