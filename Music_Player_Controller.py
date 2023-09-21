from MP3_Player import MP3_Player
from Music_List_Reader import Music_List_Reader
from GUI import GUI

class Music_Player_Controller():
    def __init__(self,GUI):
        self.GUI=GUI
        music_list_reader = Music_List_Reader() #se crea la instancia encargada del manejo de lectura
        self.song_list = music_list_reader.read_file() #se lee el archivo de las canciones y se almacena en una lista
        self.load_songs_GUI()
        
    def load_songs_GUI(self)    :
        self.GUI.song_list= self.song_list
    def play_song(self):
        
        pass
    def pause_song(self):
        pass
    def unpause_song(self):
        pass
    def next_song(self):
        pass
    def play_raw_song(self,path):
        pass
    def add_song(self,path):
        pass

        

    