import yt_dlp
from tkinter import *


def paste():
    entry.delete(0, END)
    entry.insert(0, root.clipboard_get())

def download_audio():
    url = entry.get()
    if url:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except yt_dlp.utils.DownloadError:
            label2.config(text="Ошибка загрузки. Проверьте ссылку на видео.")
        except Exception as e:
            label2.config(text=f"Произошла ошибка: {str(e)}")
    else:
        label2.config(text="Введите корректную ссылку.")


root = Tk()
root.geometry("400x300")
root.title("mp3 from youtube")

label = Label(root, text="Введите ссылку на видео на ютубе")
label.pack(pady=10)

entry = Entry(root, width=50)
entry.event_add('<<Paste>>', '<Control-igrave>')
entry.pack(pady=10)
entry.focus_set()


button = Button(root, text="Скачать", command=download_audio)
button.pack(pady=20)

paste_button = Button(root, text="Вставить", command=paste)
paste_button.pack(pady=30)

label2 = Label(root, text="")
label2.pack(pady=10)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

root.mainloop()
