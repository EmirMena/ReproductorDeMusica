import tkinter as tk
from MP3_Player import MP3_Player
from Music_List_Reader import Music_List_Reader

class window():

    def __init__(self):
        self.window = tk.Tk()
        self.MP3_Player_model = MP3_Player()

    def configure_window(self):
        self.window.title("Reproductor de Audio")
        self.window.geometry("700x140")

        # Botones
        play_button = tk.Button(self.window, text="Reproducir", command=self.MP3_Player_model.play_audio)
        pause_button = tk.Button(self.window, text="Pausa", command=self.MP3_Player_model.pause_audio)
        unpause_button = tk.Button(self.window, text="Continuar", command=self.MP3_Player_model.unpause_audio)
        #stop_button = tk.Button(self.window, text="Detener", command=self.MP3_Player_model.stop_audio)
        next_button = tk.Button(self.window, text="Siguiente", command=self.MP3_Player_model.next_song)
        
        # Colocar botones en la ventana
        play_button.grid()
        pause_button.grid()
        unpause_button.grid()
        #stop_button.pack()
        next_button.grid()

    def generate_buttons_for_songs(self):
        music_list_reader = Music_List_Reader()
        songs_list = music_list_reader.read_file()

        BUTTON_WITDH = 40  # Ancho fijo para los botones
        BUTTON_HEIGHT = 2  # Alto fijo para los botones
        row_counter = 0

        for song in songs_list:
            songs_name, autor, song_path= song[0], song[1], song[3]
            reproduction_song_button = tk.Button(self.window, text=songs_name + " from: " + autor, width=BUTTON_WITDH, height=BUTTON_HEIGHT, command=lambda path=song_path: self.MP3_Player_model.play_raw_audio(path))
            reproduction_song_button.grid(row=row_counter + 1, column=0)

            add_song_button = tk.Button(self.window, text="Add", width=BUTTON_WITDH, height=BUTTON_HEIGHT, command=lambda path=song_path: self.MP3_Player_model.add_song(path))
            add_song_button.grid(row=row_counter + 1, column=1)
            row_counter += 1
        
    def initialize_window(self):
        # Iniciar bucle de eventos de tkinter
        self.window.mainloop()