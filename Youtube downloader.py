import tkinter as tk
from pytube import YouTube
def download_video():
    global E1
    string=E1.get()
    yt=YouTube(str(string))
    print(yt.streams)
    yt.streams.first().download()
    print("Video successfuly downloaded")
root=tk.Tk()
w=tk.Label(root,text="Youtube Downloader")
w.pack()
E1=tk.Entry(root,bd=10)
E1.pack(side=tk.TOP)
button=tk.Button(root,text="Download",fg="red",command=download_video)
button.pack(side=tk.BOTTOM)
root.mainloop()
