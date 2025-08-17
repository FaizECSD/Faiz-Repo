import customtkinter as ctk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        pygame.mixer.init()

        self.current_music = None

        self.CTkLabel = ctk.CTkLabel(root, text="No music loaded", width=35)
        self.CTkLabel.pack(pady=10)

        self.play_CTkButton = ctk.CTkButton(root, text="Play", command=self.play_music)
        self.play_CTkButton.pack(pady=5)

        self.pause_CTkButton = ctk.CTkButton(root, text="Pause", command=self.pause_music)
        self.pause_CTkButton.pack(pady=5)

        self.stop_CTkButton = ctk.CTkButton(root, text="Stop", command=self.stop_music)
        self.stop_CTkButton.pack(pady=5)

        self.load_CTkButton = ctk.CTkButton(root, text="Load Music", command=self.load_music)
        self.load_CTkButton.pack(pady=5)

    def load_music(self):
        self.current_music = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3 *.wav")])
        if self.current_music: 
            self.CTkLabel.configure(text=f"Loaded: {self.current_music.split('/')[-1]}")
            self.paused=False
            self.pause_time=0
            

    def play_music(self):
        if self.current_music: 
            if self.paused: 
                pygame.mixer.music.unpause() 
                self.paused = False 
            else: 
                pygame.mixer.music.load(self.current_music) 
                pygame.mixer.music.play(loops=0, start=self.pause_time)

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True 
            self.pause_time = pygame.mixer.music.get_pos() / 1000 # Get position in seconds

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.paused = False 
            self.pause_time = 0

if __name__ == "__main__":
    root = ctk.CTk()
    app = MusicPlayer(root)
    root.mainloop()
