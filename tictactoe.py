import sys
import pygame
pygame.init()

screensize = 1000
colour = [0, 0, 0], [255, 255, 255], [0, 50, 0], [0, 255, 0], [50, 0, 0], [255, 0, 0]
display = pygame.display.set_mode([screensize, screensize])
pygame.display.set_caption('Tic Tac Toe')
greenClicked = [False] * 9
redClicked = [False] * 9
greenTurn = True
winning = False
ending = 0


squares = list()
for line1 in range(3):
    squares.append(pygame.Rect([(screensize / 3) * line1, 0], [(screensize / 3), (screensize / 3)]))
for line2 in range(3):
    squares.append(pygame.Rect([(screensize / 3) * line2, screensize / 3], [(screensize / 3), (screensize / 3)]))
for line3 in range(3):
    squares.append(pygame.Rect([(screensize / 3) * line3, screensize - (screensize / 3)], [(screensize / 3), (screensize / 3)]))


def grid(screen, size, color):
    space = size / 3
    for i in range(2):
        pygame.draw.line(screen, color, [space * (i + 1), 0], [space * (i + 1), size])
        pygame.draw.line(screen, color, [0, space * (i + 1)], [size, space * (i + 1)])
    # drawing lines


def clickSquares(screen, color, squareList, clickedGreen, clickedRed, turnGreen):
    if turnGreen:
        for i in range(9):
            if squareList[i].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, color[2], squareList[i])
                for action in pygame.event.get():
                    if action.type == pygame.MOUSEBUTTONDOWN:
                        clickedGreen[i] = True
                        turnGreen = False
                        if clickedRed[i] and clickedGreen[i]:
                            clickedGreen[i] = False
                            turnGreen = True
                    elif action.type == pygame.QUIT:
                        sys.exit()
            if clickedRed[i]:
                pygame.draw.rect(screen, color[5], squareList[i])
            if clickedGreen[i]:
                pygame.draw.rect(screen, color[3], squareList[i])
    else:
        for i in range(9):
            if squareList[i].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, color[4], squareList[i])
                for action in pygame.event.get():
                    if action.type == pygame.MOUSEBUTTONDOWN:
                        clickedRed[i] = True
                        turnGreen = True
                        if clickedRed[i] and clickedGreen[i]:
                            clickedRed[i] = False
                            turnGreen = False
                    elif action.type == pygame.QUIT:
                        sys.exit()
            if clickedGreen[i]:
                pygame.draw.rect(screen, color[3], squareList[i])
            if clickedRed[i]:
                pygame.draw.rect(screen, color[5], squareList[i])
    return squareList, turnGreen


def end(greenList, redList):
    trueCount = 0
    if greenList[0] and greenList[3] and greenList[6]:
        return 1
    elif greenList[1] and greenList[4] and greenList[7]:
        return 1
    elif greenList[2] and greenList[5] and greenList[8]:
        return 1
    # vertical victory lines
    elif greenList[0] and greenList[1] and greenList[2]:
        return 1
    elif greenList[3] and greenList[4] and greenList[5]:
        return 1
    elif greenList[6] and greenList[7] and greenList[8]:
        return 1
    # horizontal victory lines
    elif greenList[0] and greenList[4] and greenList[8]:
        return 1
    elif greenList[2] and greenList[4] and greenList[6]:
        return 1
    # diagonal victory lines
    if redList[0] and redList[3] and redList[6]:
        return 2
    elif redList[1] and redList[4] and redList[7]:
        return 2
    elif redList[2] and redList[5] and redList[8]:
        return 2
    # vertical victory lines
    elif redList[0] and redList[1] and redList[2]:
        return 2
    elif redList[3] and redList[4] and redList[5]:
        return 2
    elif redList[6] and redList[7] and redList[8]:
        return 2
    # horizontal victory lines
    elif redList[0] and redList[4] and redList[8]:
        return 2
    elif redList[2] and redList[4] and redList[6]:
        return 2
    for i in range(9):
        if greenList[i] or redList[i]:
            trueCount += 1
    if trueCount == 9:
        return 3


while True:
    if not winning:
        grid(display, screensize, colour[1])
        pygame.display.update()
        display.fill(colour[0])
        clickList = clickSquares(display, colour, squares, greenClicked, redClicked, greenTurn)
        greenTurn = clickList[1]
        ending = end(greenClicked, redClicked)
        for event in pygame.event.get():
            # Note to future self: calling pygame.event.get somehow stops a crash
            if event.type == pygame.QUIT:
                sys.exit()
    if ending == 1:
        winning = True
        pygame.display.update()
        display.fill(colour[0])
        font = pygame.font.Font('tictactoe\Freesansbold.ttf', 50)
        text = font.render('Green wins', True, colour[1], colour[0])
        text_rect = text.get_rect()
        text_rect.center = (screensize/2, screensize/2)
        display.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                greenClicked = [False] * 9
                redClicked = [False] * 9
                greenTurn = True
                winning = False
                ending = 0
            if event.type == pygame.QUIT:
                sys.exit()
    if ending == 2:
        winning = True
        pygame.display.update()
        display.fill(colour[0])
        font = pygame.font.Font('tictactoe\Freesansbold.ttf', 50)
        text = font.render('Red wins', True, colour[1], colour[0])
        text_rect = text.get_rect()
        text_rect.center = (screensize / 2, screensize / 2)
        display.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                greenClicked = [False] * 9
                redClicked = [False] * 9
                greenTurn = True
                winning = False
                ending = 0
            if event.type == pygame.QUIT:
                sys.exit()
    if ending == 3:
        winning = True
        pygame.display.update()
        display.fill(colour[0])
        font = pygame.font.Font('tictactoe\Freesansbold.ttf', 50)
        text = font.render('Draw', True, colour[1], colour[0])
        text_rect = text.get_rect()
        text_rect.center = (screensize / 2, screensize / 2)
        display.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                greenClicked = [False] * 9
                redClicked = [False] * 9
                greenTurn = True
                winning = False
                ending = 0
            if event.type == pygame.QUIT:
                sys.exit()
