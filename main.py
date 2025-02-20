import tkinter as tk
from pytube import YouTube
import youtube_dl
from tkinter import messagebox

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube İndirici")
        self.root.geometry("400x200")

        self.root.grid_rowconfigure(0, weight=1)  
        self.root.grid_columnconfigure(0, weight=1) 
        self.root.grid_columnconfigure(1, weight=1) 

        self.video_button = tk.Button(root, text="Video İndir", command=self.show_video_page)
        self.video_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)

        self.music_button = tk.Button(root, text="Müzik İndir", command=self.show_music_page)
        self.music_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)

        self.video_frame = tk.Frame(root)
        self.music_frame = tk.Frame(root)

        self.create_video_page()
        self.create_music_page()

        self.current_page = None

    def show_video_page(self):
        self.hide_main_buttons()
        self.video_frame.pack(fill=tk.BOTH, expand=True)
        self.current_page = self.video_frame

    def show_music_page(self):
        self.hide_main_buttons()
        self.music_frame.pack(fill=tk.BOTH, expand=True)
        self.current_page = self.music_frame

    def hide_main_buttons(self):
        self.video_button.grid_forget()
        self.music_button.grid_forget()

    def create_video_page(self):
        self.video_link_label = tk.Label(self.video_frame, text="YouTube Linki:")
        self.video_link_label.pack(pady=5)
        self.video_link_entry = tk.Entry(self.video_frame, width=40)
        self.video_link_entry.pack(pady=5)

        self.video_download_button = tk.Button(self.video_frame, text="İndir", command=self.download_video)
        self.video_download_button.pack(pady=10)

        self.video_status_label = tk.Label(self.video_frame, text="")
        self.video_status_label.pack()

        self.video_back_button = tk.Button(self.video_frame, text="Geri", command=lambda: self.show_main_buttons())
        self.video_back_button.pack(pady=5)

    def create_music_page(self):
        self.music_link_label = tk.Label(self.music_frame, text="YouTube Linki:")
        self.music_link_label.pack(pady=5)
        self.music_link_entry = tk.Entry(self.music_frame, width=40)
        self.music_link_entry.pack(pady=5)

        self.music_download_button = tk.Button(self.music_frame, text="İndir", command=self.download_music)
        self.music_download_button.pack(pady=10)

        self.music_status_label = tk.Label(self.music_frame, text="")
        self.music_status_label.pack()

        self.music_back_button = tk.Button(self.music_frame, text="Geri", command=lambda: self.show_main_buttons())
        self.music_back_button.pack(pady=5)

    def download_video(self):
        link = self.video_link_entry.get()
        try:
            yt = YouTube(link)
            ys = yt.streams.get_highest_resolution()
            ys.download()
            self.video_status_label.config(text="Video İndirildi.", fg="green")
            messagebox.showinfo("Başarılı","Video İndirme işlemi tamamlandı.")
        except Exception as e:
            self.video_status_label.config(text=f"Hata: {e}", fg="red")
            messagebox.showerror("Hata",f"Video indirilirken bir hata oluştu: {e}")

    def download_music(self):
        link = self.music_link_entry.get()
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'mp3',
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_title = info_dict.get('title', None)
                self.music_status_label.config(text="Müzik İndirildi.", fg="blue")
                messagebox.showinfo("Başarılı","Müzik İndirme işlemi tamamlandı.")
        except Exception as e:
            self.music_status_label.config(text=f"Hata: {e}", fg="red")
            messagebox.showerror("Hata",f"Müzik indirilirken bir hata oluştu: {e}")

    def show_main_buttons(self):
        self.hide_current_page()
        self.video_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
        self.music_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
        self.current_page = None

    def hide_current_page(self):
        if self.current_page:
            self.current_page.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
