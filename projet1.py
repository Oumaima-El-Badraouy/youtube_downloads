import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import * 

#  settings:"System""Light" or "Dark"
set_appearance_mode("System") 
set_default_color_theme("blue") # theme
for i in os.listdir(os.getcwd()):
    if i == "youtube_downloads":
        break
else:    
    os.mkdir("youtube_downloads")

# Download video  had entry_field howa lvalue
def download_video(entry_field):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        
        # calité dyal lvideo
        
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()

        # Showing the download time in a new window
        popup = CTk()
        popup.title("Download Status")
        popup.resizable(False, False)
        popup.geometry("200x100")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure((0,1), weight=1)
        
        # hna kay3tk msg + lw9t dlvideo mnin kaytchrg
        
        msg = StringVar()
        msg.set(f"Download successful!\nTotal time taken: {round(end_time-start_time,3)} seconds")
        label = CTkLabel(popup, text=msg.get())
        label.grid(row=0, column=0)
        button = CTkButton(popup, text="OK", command=popup.destroy)
        button.grid(row=1, column=0)
        popup.mainloop()
        
    except exceptions.RegexMatchError: #  invalid link or empty link, show an error message
        error = CTk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x100")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = CTkLabel(error, text="Please enter a valid YouTube link")
        error_label.grid(row=0, column=0)
        
        button = CTkButton(error, text="OK", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()

# layout dyale app
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x150")
master.resizable(False, False)
CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)
entry = CTkEntry(master)
entry.grid(row=0, column=1)
CTkButton(master, text='Download', command=lambda *args: download_video(entry.get())).grid(row=1, column=0, columnspan=2)
master.mainloop()