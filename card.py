import pygame.image
import pygame.transform
from pygame.locals import *
from settings import card_size, card_height, card_width

cardback = pygame.image.load("resources/cardback.jpg")
cardback = pygame.transform.rotate(cardback, 90)
cardback = pygame.transform.scale(cardback, card_size)

bombImage = pygame.image.load("resources/bomb.png")
bombImage = pygame.transform.scale(bombImage, card_size)

dickImage = pygame.image.load("resources/dick.png")
dickImage = pygame.transform.scale(dickImage, card_size)

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
        if self.surface == cardback:
            if(self.name == 'bomb'):
                self.surface = bombImage
            elif(self.name == 'Dick'):
                self.surface = dickImage
            else:
                self.surface = self.front
        else:
            self.surface = cardback
