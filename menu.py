import pygame
import webbrowser
import sys


pygame.init()

res = (700, 800)

pygame.mixer.music.load('sound/war.mp3')
pygame.mixer.music.play()
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Alien war")
bg = pygame.image.load('images/Fone-for-Load.png')
rect = bg.get_rect()
screen.blit(bg, rect)

# white color
color = (255, 255, 255)
colorTEXT = (0, 0, 0)
colorCapA = (0, 191, 255)
colorCapW = (30, 144, 255)
colorMus1 = (255, 0, 0)
colorMus1_2 = (139, 0, 0)
colorMus2 = (0, 255, 0)
colorMus2_2 = (0, 139, 0)

# light shade of the button
color_light = (25, 65, 247)
color_light2 = (25, 65, 247)

# dark shade of the button
color_dark = (4, 196, 246)
color_dark2 = (4, 196, 246)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Serif', 48)
# rendering a text written in
# this font
text = smallfont.render('Leave', True, color)
play = smallfont.render('Play', True, color)
ab = smallfont.render('About us', True, color)
capA = bigfont.render('Alien', True, colorCapA)
capW = bigfont.render('War', True, colorCapW)
Mus = bigfont.render('Music', True, colorCapA)
OFF = smallfont.render('Off', True, colorTEXT)
ON = smallfont.render('On', True, colorTEXT)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                pygame.quit()

            if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 6 <= mouse[1] <= height / 6 + 40:
                import TCL

            if width / 1.9 <= mouse[0] <= width / 1.9 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.mixer.music.load('sound/JustM.mp3')
                pygame.mixer.music.play(-1)


            if width / 3.4 <= mouse[0] <= width / 3.4 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.mixer.music.stop()

            if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 4 <= mouse[1] <= height / 4 + 40:
                #                print('Позже тут будет открываться сайт')
                webbrowser.open('http://127.0.0.1:8000/', new=0)

                # fills the screen with a color
        #    screen.fill((42, 144, 243))
        #    pygame.display.flip()

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
        pygame.draw.rect(screen, color_light, [width / 2.5, height / 3, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2.5, height / 3, 140, 40])

    if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 6 <= mouse[1] <= height / 6 + 40:
        pygame.draw.rect(screen, color_light2, [width / 2.5, height / 6, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark2, [width / 2.5, height / 6, 140, 40])

    if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 4 <= mouse[1] <= height / 4 + 40:
        pygame.draw.rect(screen, color_light2, [width / 2.5, height / 4, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark2, [width / 2.5, height / 4, 140, 40])


    if width / 3.4 <= mouse[0] <= width / 3.4 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, colorMus1, [width / 3.4, height / 2, 140, 40])


    else:
        pygame.draw.rect(screen, colorMus1_2, [width / 3.4, height / 2, 140, 40])

    if width / 1.9 <= mouse[0] <= width / 1.9 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, colorMus2, [width / 1.9, height / 2, 140, 40])


    else:
        pygame.draw.rect(screen, colorMus2_2, [width / 1.9, height / 2, 140, 40])


        # superimposing the text onto our button
    screen.blit(text, (width / 2.5 + 37, height / 3))
    screen.blit(play, (width / 2.5 + 47, height / 6))
    screen.blit(ab, (width / 2.5 + 14, height / 4))
    screen.blit(capA, (width / 2.9 + 14, height / 14))
    screen.blit(capW, (width / 2 + 14, height / 14))
    screen.blit(Mus, (width / 2.5 + 14, height / 2.5))
    screen.blit(OFF, (width / 2.9 + 14, height / 2))
    screen.blit(ON, (width / 1.7 + 14, height / 2))


    # updates the frames of the game
    pygame.display.update()
