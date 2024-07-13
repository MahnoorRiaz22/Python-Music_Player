import tkinter as tk
from pygame import mixer
from tkinter import *
# Import ttk for the combobox and progress bar
from tkinter import ttk
import os

# Initialize the main window
root = Tk()
root.title("Music Player Application")
root.geometry("450x250")
root.config(bg="Gray")

# Initialize the current song index
current_song_index = -1
def set_image():
    img = tk.PhotoImage(file='G:\\users\\album_images\\Background.png')
    img_lb.config(image=img)
    img_lb.image = img

img_lb = tk.Label(root)
img_lb.grid(row=0, column=1, columnspan=5, pady=10)

def previous_music():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
        # Update the playlist selection to the previous song
        playlist.current(current_song_index)
        play_selected_song()
    else:
        print("No Previous Song")
def play_music():
    global current_song_index
    # Get the index of the selected song
    current_song_index = playlist.current()
    play_selected_song()

def play_selected_song():
    global current_song_index
    currentsong = playlist.get()
    print(currentsong)
    mixer.music.load(currentsong)
    musicStatus.set("Playing")
    mixer.music.play()
    update_progress_bar()

def next_music():
    global current_song_index
    if current_song_index < len(music) - 1:
        current_song_index += 1
        playlist.current(current_song_index)
        play_selected_song()
    else:
        print("No Next Song")

def stop_music():
    musicStatus.set("Stopped")
    mixer.music.stop()
    # Reset progress bar
    progress_bar['value'] = 0

def pause_music():
    musicStatus.set("Paused")
    mixer.music.pause()

def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

def update_progress_bar():
    if mixer.music.get_busy():
        progress_bar['value'] = (mixer.music.get_pos() / 1000)
        root.after(1000, update_progress_bar)


# Initialize mixer and variables
mixer.init()
musicStatus = StringVar()
musicStatus.set("Choosing")

# Create and populate the playlist as a Combobox
os.chdir(r"G:\users\music")
music = os.listdir()

playlist = ttk.Combobox(root, values=music, state="readonly", width=40)
playlist.grid(row=2, column=1, columnspan=4)

# Add buttons for music control
previousbtn = ttk.Button(root, text="◀|", command=previous_music)
previousbtn.grid(row=4, column=1)

playbtn = ttk.Button(root, text="▶", command=play_music)
playbtn.grid(row=4, column=2)

stopbtn = ttk.Button(root, text="◼", command=stop_music)
stopbtn.grid(row=4, column=3)

pausebtn = ttk.Button(root, text="||", command=pause_music)
pausebtn.grid(row=4, column=4)

nextbtn = ttk.Button(root, text="|▶", command=next_music)
nextbtn.grid(row=4, column=5)

# Add a volume control slider
volumeslider = Scale(root, from_=0, to=100, orient="vertical", command=set_volume, bg="black", fg="white")
volumeslider.set(50)  # Set default volume to 50%
volumeslider.grid(row=0, column=5, columnspan=5, pady=5)

# Add a progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress_bar.grid(row=3, column=0, columnspan=5, pady=10)

set_image()
mainloop()
