from pytube import YouTube
from tkinter import *
import youtube_dl

window = Tk()
window.title("-MP4 & MP3 DOWLOAD-")
window.geometry("300x250")
l1 = Label(window, text="********** LİNK **********",fg="red")
l1.place(x=90, y=15)
def mp4indir():
    link = e1.get()
    link = str(link)
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    l3.config(text=f"Mp4 İndirildi.",fg="green")

def mp3indir():
    link = e1.get()
    link = str(link)
    vb = youtube_dl.YoutubeDL().extract_info(url=link,download=False)
    da = f"{vb['title']}.mp3"
    ayarlar = {
        'format':'bestaudio',
        'keepvideo': False,
        'outtmpl':da,}
    with youtube_dl.YoutubeDL(ayarlar)as ydl:
        ydl.download([vb['webpage_url']])
    l3.config(text=f"Mp3 İndirildi.",fg="blue")
e1 = Entry(window, width=25)
e1.place(x=80,y=45)
bt = Button(window, text="MP4 DOWLOAD", padx="20",pady="5", command=mp4indir,fg="green")
bt.place(x=90,y=80)
bt2 = Button(window, text="MP3 DOWLOAD", padx="20",pady="5", command=mp3indir,fg="blue")
bt2.place(x=90,y=120)
l3 = Label(window)
l3.place(x=120,y=170)
window.mainloop()
