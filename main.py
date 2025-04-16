import tkinter as tk
from tkinter import ttk, messagebox
#from pytube import YouTube # python 3.13 ve 3.12.0'dan itibaren pytube modülü youtube-dl ile değiştirildi.)
#import youtube_dl   # python 3.13 ve 3.12.0'dan itibaren youtube-dl modülü pytube ile değiştirildi.

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube İndirici")
        self.root.geometry("270x250")
        self.root.resizable(False, False) 

        self.style = ttk.Style(root)
        self.style.theme_use('clam')

        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    
        button_style = ttk.Style()
        button_style.configure('TButton', padding=10, font=('Segoe UI', 10))

        self.video_button = ttk.Button(self.main_frame, text="Video İndir", command=self.show_video_page, style='TButton')
        self.video_button.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.music_button = ttk.Button(self.main_frame, text="Müzik İndir", command=self.show_music_page, style='TButton')
        self.music_button.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        self.video_frame = ttk.Frame(root, padding=10)
        self.music_frame = ttk.Frame(root, padding=10)

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
        self.video_button.pack_forget()
        self.music_button.pack_forget()

    def create_video_page(self):
        link_label = ttk.Label(self.video_frame, text="YouTube Linki:", font=('Segoe UI', 10))
        link_label.pack(pady=5, anchor="w")
        self.video_link_entry = ttk.Entry(self.video_frame, width=45, font=('Segoe UI', 10))
        self.video_link_entry.pack(pady=5, fill="x")

        download_button = ttk.Button(self.video_frame, text="İndir", command=self.download_video, style='TButton')
        download_button.pack(pady=15)

        self.video_status_label = ttk.Label(self.video_frame, text="", font=('Segoe UI', 9), foreground="gray")
        self.video_status_label.pack(pady=5, anchor="w")

        back_button = ttk.Button(self.video_frame, text="Geri", command=self.show_main_buttons, style='TButton')
        back_button.pack(pady=10)

    def create_music_page(self):
        link_label = ttk.Label(self.music_frame, text="YouTube Linki:", font=('Segoe UI', 10))
        link_label.pack(pady=5, anchor="w")
        self.music_link_entry = ttk.Entry(self.music_frame, width=45, font=('Segoe UI', 10))
        self.music_link_entry.pack(pady=5, fill="x")

        download_button = ttk.Button(self.music_frame, text="İndir", command=self.download_music, style='TButton')
        download_button.pack(pady=15)

        self.music_status_label = ttk.Label(self.music_frame, text="", font=('Segoe UI', 9), foreground="gray")
        self.music_status_label.pack(pady=5, anchor="w")

        back_button = ttk.Button(self.music_frame, text="Geri", command=self.show_main_buttons, style='TButton')
        back_button.pack(pady=10)

    def download_video(self):
        link = self.video_link_entry.get()
        try:
            yt = YouTube(link)
            ys = yt.streams.get_highest_resolution()
            self.video_status_label.config(text="İndiriliyor...", foreground="orange")
            ys.download()
            self.video_status_label.config(text="Video İndirildi.", foreground="green")
            messagebox.showinfo("Başarılı", "Video İndirme işlemi tamamlandı.")
        except Exception as e:
            self.video_status_label.config(text=f"Hata: {e}", foreground="red")
            messagebox.showerror("Hata", f"Video indirilirken bir hata oluştu: {e}")

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
            self.music_status_label.config(text="İndiriliyor...", foreground="orange")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_title = info_dict.get('title', None)
                self.music_status_label.config(text="Müzik İndirildi.", foreground="blue")
                messagebox.showinfo("Başarılı", "Müzik İndirme işlemi tamamlandı.")
        except Exception as e:
            self.music_status_label.config(text=f"Hata: {e}", foreground="red")
            messagebox.showerror("Hata", f"Müzik indirilirken bir hata oluştu: {e}")

    def show_main_buttons(self):
        self.hide_current_page()
        self.video_button.pack(pady=15, padx=10, fill="x")
        self.music_button.pack(pady=15, padx=10, fill="x")
        self.current_page = None

    def hide_current_page(self):
        if self.current_page:
            self.current_page.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
