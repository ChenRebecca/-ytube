import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import threading


def click_func():
    url = yt_url.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror('錯誤', 'pytube 不支援此影片或者網址錯誤')
        return

    yt = YouTube(url)
    if messagebox.askyesno('確認方塊', f'是否下載{yt.title}影片？'):
        yt.streams.first().download()
    else:
        print('取消下載')


window = tk.Tk()
window.geometry('640x480')
window.title('YouTube 極速下載器')

input_fm = tk.Frame(window, bg='red', width=640, height=480)
input_fm.pack(side="top", fill="both", expand=True)

lb = tk.Label(input_fm, bg='red', fg='white', text='請輸入YouTube 網址', font=('細明體', 40))
lb.pack(side="top",pady=70)
yt_url = tk.StringVar()

entry = tk.Entry(input_fm, textvariable=yt_url, width=70)
entry.pack(side='top',pady=70)

btn = tk.Button(input_fm, text='下載影片', command=click_func, bg='#FFD700', fg='Black', font=('細明體', 30))
btn.pack(side='top')

window.mainloop()
