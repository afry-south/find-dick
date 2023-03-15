import math

import requests
import json
import sys
from collections import defaultdict
import random
import pygame
from pygame.locals import *
#from slack import SlackBot
from slack_mock import SlackBot
from card import Card
from settings import card_size, card_height, card_width

token = input('enter bot token\n')
emails = input("enter emails. Example: _\n").split(',')
print(emails)
slackbot = SlackBot(token)
dick_card = "Dick"
bomb_card = "bomb"

size_of_deck = 16
def create_deck():
    deck = []
    for i in range(1, size_of_deck - 2):
        deck.append('hjärter '+str(i))
        deck.append('spader '+str(i))
        deck.append('ruter '+str(i))
        deck.append('klöver '+str(i))
    return deck


# 4*4 kort + Dick + bomb
def create_board():
    deck = create_deck()
    random.shuffle(deck)
    board = deck[:size_of_deck-16]
    board.append(dick_card)
    board.append(bomb_card)
    board.append('Daniel')
    board.append('Ronnie')
    board.append('Marcos')
    board.append('Per')
    board.append('Erica')
    board.append('Dennis')
    board.append('Carl')
    board.append('Patrik')
    board.append('Hampus')
    board.append('Chadvin')
    board.append('Lisa')
    board.append('Oscar')
    board.append('Björn')
    board.append('Johan')
    random.shuffle(board)
    return board


def right_or_left(findex, cindex, card):
    if findex % math.sqrt(size_of_deck) < cindex % math.sqrt(size_of_deck):
        return 'Dick är vänster om ' + card
    elif findex % math.sqrt(size_of_deck) > cindex % math.sqrt(size_of_deck):
        return 'Dick är höger om ' + card
    else:
        return ''


def up_or_down(findex, cindex, card):
    if int(findex / math.sqrt(size_of_deck)) > int(cindex / math.sqrt(size_of_deck)):
        return 'Dick är nedanför ' + card
    elif int(findex / math.sqrt(size_of_deck)) < int(cindex / math.sqrt(size_of_deck)):
        return 'Dick är ovanför ' + card
    else:
        return ''


def create_clues(board):
    clues = []
    for card in board:
        if card != dick_card and card != bomb_card:
            cindex = board.index(card)
            clue1 = right_or_left(dick_index, cindex, card)
            if clue1 != '':
                clues.append(clue1)
            clue2 = up_or_down(dick_index, cindex, card)
            if clue2 != '':
                clues.append(clue2)
            
    random.shuffle(clues)
    return clues


board = create_board()
dick_index = board.index(dick_card)
bomb_index = board.index(bomb_card)

clues = create_clues(board)
# print(clues)
users = defaultdict(dict)

for email in emails:
    users[email]=slackbot.getUserId(email)

for user in users:
    slackbot.sendMessage(users[user], 'Dick har försvunnit under mystiska omständigheter! Senast sågs han gömd i denna kortlek - kasta er in och släpp honom fri. Men se upp! En skojare har klämt in en bomb i kortleken i hopp om att säkerställa misslyckande. Använd de utströdda ledtrådarna, se igenom skojarens lustigheter, undvik bomben och rädda Dick ut ur kortleken!')

randomUsers= list(users.keys())
random.shuffle(randomUsers)
impostors = randomUsers[:1]

for impostor in impostors:
    slackbot.sendMessage(users[impostor], 'Hej, du är en skojare, ditt uppdrag är att lura de andra deltagarna med falska ledtrådar.\nBomben är på rad: ' + str(int(bomb_index / 4) + 1) + ' och kolumn: ' + str(int(bomb_index % 4) + 1) + '\nDick är på rad: ' + str(int(dick_index / 4) + 1) + ' och kolumn: ' + str(int(dick_index % 4) + 1))


def send_random_clue(user):
    slackbot.sendMessage(users[user], clues[0])
    random.shuffle(clues)


# GUI code
windowSurface = pygame.display.set_mode((1200, 700), 0 , 32)
pygame.display.set_caption('Find Dick')

cards = [Card(s) for s in board]
pygame.font.init()
basicFont = pygame.font.SysFont("dejavusans", size_of_deck-2)


buttons = []
y = 60
buttonHeight = 30
for player in users:
    print(player)
    button = pygame.Surface((400, buttonHeight))
    button.fill((200, 100, 100))
    text = basicFont.render(player, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.centerx = button.get_rect().centerx
    textRect.centery = button.get_rect().centery
    button.blit(text, textRect)
    rect = windowSurface.blit(button, (500, y))
    y += buttonHeight+2
    buttons.append((rect, player))


def render():
    visible_cards = []
    x = 0
    y = 0
    for card in cards:
        x_pos = x*(card_width + 5)
        y_pos = y*(card_height + 5)
        rect = windowSurface.blit(card.surface, (x_pos, y_pos))
        visible_cards.append((rect, card))
        x += 1
        if x > math.sqrt(size_of_deck) - 1:
            x = 0
            y += 1
    return visible_cards


visibleCards = render()
# Draw the window onto the screen
pygame.display.update()

# Run the game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_cards = [s[1] for s in visibleCards if s[0].collidepoint(pos)]
            for card in clicked_cards:
                card.flip()
            clicked_buttons = [s[1] for s in buttons if s[0].collidepoint(pos)]
            for button in clicked_buttons:
                send_random_clue(button)

    visibleCards = render()
    pygame.display.update()
    clock.tick(30)



# while True:
#     for user in users:
#         adminInput = input('press 1 for sending clue to ' + user + ' press anything else to continue'+ '\n')
#         print(adminInput)
#         if adminInput == '1':
#             slackbot.sendMessage(users[user], clues[0])
#             print('message sent to ' + user + ' message ' + clues[0])
#             random.shuffle(clues)

