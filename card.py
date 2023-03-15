import pygame.image
import pygame.transform
from pygame.locals import *
from sound import Sound
from settings import card_size, card_height, card_width
from settings import bomb_sound, found_sound, game_over_sound

cardback = pygame.image.load("resources/cardback.jpg")
cardback = pygame.transform.rotate(cardback, 90)
cardback = pygame.transform.scale(cardback, card_size)

pygame.font.init()
basicFont = pygame.font.SysFont("dejavusans", 14)

# for font in pygame.font.get_fonts():
#     print(font)


class Card:
    front = None
    surface = cardback
    name = ""

    def __init__(self, name):
        self.name = name
        self.front = pygame.Surface((card_width, card_height))
        self.front.fill((100, 100, 200))
        text = basicFont.render(name, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.centerx = self.front.get_rect().centerx
        textRect.centery = self.front.get_rect().centery
        self.front.blit(text, textRect)

    def flip(self):
        s = Sound()
        if self.surface == cardback:
            self.surface = self.front
        else:
            s.surface = cardback
        #Play sound
        s.play(self.name)    
        
