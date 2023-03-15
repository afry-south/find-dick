from pygame import mixer
import random
from settings import bomb_sound, found_sound, game_over_sound, sound_file_extension, sound_dir

class Sound :

    def __init__(self):
        mixer.init()
        mixer.music.set_volume(0.9)


    def play(self, song) :
        if "hjärter" in song or "spader" in song or "klöver" in song or "ruter" in song :
            song = "default"
        path = sound_dir + "/" + str(song).lower()
        if song == "default" or song == "Dick" or song == "bomb" :
            path += str(random.randint(0,8))
        path += "." + sound_file_extension
        mixer.music.load(path)
        mixer.music.play()








