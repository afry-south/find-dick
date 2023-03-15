from pygame import mixer
import os
import random
from settings import bomb_sound, found_sound, game_over_sound, sound_file_extension, sound_dir
from os.path import exists
class Sound :

    def __init__(self):
        mixer.init()
        mixer.music.set_volume(0.9)


    def play(self, song) :
    
        #print("SONG: " + song)
        if "hjärter" in song or "spader" in song or "klöver" in song or "ruter" in song :
            song = "default"
            
        if song == "default" or song == "Dick" or song == "bomb" :
            path = sound_dir + "/" + str(song).lower() + str(random.randint(0,8)) + "." + sound_file_extension
        
        else :
        
            list = os.listdir(sound_dir)
            #print(list)
            #print(song + "0." + sound_file_extension)
            tmp = song + "0." + sound_file_extension
            if tmp.lower() not in list :
                path = sound_dir + "/" + "default" + str(random.randint(0,8)) + "." + sound_file_extension
            else :
        
                path = sound_dir + "/" + str(song).lower() + "0." + sound_file_extension
            
        #print("PATH: " + path)
        mixer.music.load(path)
        mixer.music.play()








