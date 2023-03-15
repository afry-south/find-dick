import pygame.image
import pygame.transform
from pygame.locals import *
from os.path import exists
from sound import Sound


pygame.font.init()
basicFont = pygame.font.SysFont("dejavusans", 14)

# for font in pygame.font.get_fonts():
#     print(font)


class Card:
    front = None
    name = ""

    def __init__(self, name, card_width, card_height):
        self.name = name
        self.card_size = (card_width, card_height)
        cardback = pygame.image.load("resources/cardback.jpg")
        cardback = pygame.transform.rotate(cardback, 90)
        self.cardback = pygame.transform.scale(cardback, self.card_size)
        self.surface = self.cardback
        self.front = pygame.Surface(self.card_size)
        self.front.fill((100, 100, 200))
        text = basicFont.render(name, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.centerx = self.front.get_rect().centerx
        textRect.centery = self.front.get_rect().centery
        self.front.blit(text, textRect)

    def flip(self):
        s = Sound()
        if self.surface == self.cardback:
            self.surface = self.loadImage()
        else:
            self.surface = self.cardback
        s.play(self.name)

    def loadImage(self):
        if (exists("resources/" + self.name + ".png")):
            image = pygame.image.load("resources/" + self.name + ".png")
            return pygame.transform.scale(image, self.card_size)
        else:
            return self.front
