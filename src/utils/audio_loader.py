import os
import random
import pygame as pg
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
ASSET_DIR = ROOT_DIR / "assets"
#under assets
MUSIC_DIR = ASSET_DIR / "music"
SFX_DIR = ASSET_DIR / "sfx"

class AudioLoader:
    
    
    @staticmethod
    def stop_sound():
        pg.mixer.music.stop()
        pg.mixer.stop()
    
    # get the file strings for a set of bgm
    @staticmethod
    def get_bgms():
        return [
            MUSIC_DIR / "bgm1.wav",
            MUSIC_DIR / "bgm2.ogg"
        ]

    @staticmethod
    def get_boss_bgms():
        return [
            MUSIC_DIR / "boss1.ogg",
            MUSIC_DIR / "boss2.wav"
        ]
     
        
    @staticmethod
    def pickup_sound():
        shot = pg.mixer.Sound(SFX_DIR / "pickup.ogg")
        shot.set_volume(1)
        shot.play()
        
    @staticmethod
    def explosion_sound():
        sound = pg.mixer.Sound(SFX_DIR / "explosion.wav")
        sound.set_volume(0.28)
        sound.play()
    
    @staticmethod
    def play_meow():
        meow = pg.mixer.Sound(SFX_DIR / "meow.wav")
        meow.play()
        
    @staticmethod
    def attack_sound(file_name):
        sound = pg.mixer.Sound(str(SFX_DIR / f"{file_name}.wav"))
        if file_name == "enemyshoot":
            sound.set_volume(0.1)
        elif file_name == "shoot":
            sound.set_volume(0.10)
        else:
            sound.set_volume(0.25)
        sound.play()
      
    @staticmethod
    def crunch_sound():
        sound = pg.mixer.Sound(SFX_DIR / "crunch.mp3")
        sound.set_volume(0.3)
        sound.play()
  
    @staticmethod
    def get_shots():
        return [
            SFX_DIR / "meow.m4a"
        ]


    @staticmethod
    def play_start_music():
        if pg.mixer.music.get_busy(): # prevents the mixer from layering another instance of the music
            return
        pg.mixer.music.load(MUSIC_DIR / "start.wav")
        pg.mixer.music.set_volume(0.3) # 50% vol
        pg.mixer.music.play(-1) # -1 plays the music on an indefinite loop
        
    
    @staticmethod
    def play_end_music():
        if pg.mixer.music.get_busy(): # prevents the mixer from layering another instance of the music
            return
        pg.mixer.music.load(MUSIC_DIR / "end.wav")
        pg.mixer.music.set_volume(0.3) # 50% vol
        pg.mixer.music.play(-1) # -1 plays the music on an indefinite loop
        
        
    @staticmethod
    def play_menu_music():
        if pg.mixer.music.get_busy(): # prevents the mixer from layering another instance of the music
            return
        pg.mixer.music.load(MUSIC_DIR / "charsel.ogg")
        pg.mixer.music.set_volume(0.2) # 50% vol
        pg.mixer.music.play(-1) # -1 plays the music on an indefinite loop
    
    @staticmethod
    def play_story_audio():
        speech = pg.mixer.Sound(MUSIC_DIR / "story.mp3")
        if pg.mixer.music.get_busy() or speech.get_num_channels() > 0: # prevents the mixer from layering another instance of the music
            return
        pg.mixer.music.load(MUSIC_DIR / "military.wav")
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play()
        speech.play()
        

    @staticmethod
    def play_bgm():
        if pg.mixer.music.get_busy():
            return
        musics = AudioLoader.get_bgms()
        filename = random.choice(musics)
        pg.mixer.music.load(filename)
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play()
    
    @staticmethod
    def play_boss_bgm():
        if pg.mixer.music.get_busy():
            return
        musics = AudioLoader.get_boss_bgms()
        filename = random.choice(musics)
        pg.mixer.music.load(filename)
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play()