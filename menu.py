import pygame
import webbrowser
import sys


pygame.init()

res = (700, 800)

pygame.mixer.music.load('sound/war.mp3')
pygame.mixer.music.play()
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Alien war")
menu_bg = pygame.image.load('images/fone.png')

# white color
color = (255, 255, 255)

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

# rendering a text written in
# this font
text = smallfont.render('Leave', True, color)
play = smallfont.render('Play', True, color)
ab = smallfont.render('About us', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 3 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                pygame.quit()

            if width / 6 <= mouse[0] <= width / 2 + 140 and height / 6 <= mouse[1] <= height / 6 + 40:
                import TCL


            if width / 4 <= mouse[0] <= width / 2 + 140 and height / 4 <= mouse[1] <= height / 4 + 40:
#                print('Позже тут будет открываться сайт')
                webbrowser.open('http://127.0.0.1:8000/', new=0)

                # fills the screen with a color
#    screen.fill((42, 144, 243))
#    pygame.display.flip()
    bg = pygame.image.load('images/nebo.png')
    rect = bg.get_rect()
    screen.blit(bg, rect)
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 3 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
        pygame.draw.rect(screen, color_light, [width / 2.5, height / 3, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2.5, height / 3, 140, 40])

    if width / 6 <= mouse[0] <= width / 2 + 140 and height / 6 <= mouse[1] <= height / 6 + 40:
        pygame.draw.rect(screen, color_light2, [width / 2.5, height / 6, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark2, [width / 2.5, height / 6, 140, 40])

    if width / 4 <= mouse[0] <= width / 2 + 140 and height / 4 <= mouse[1] <= height / 4 + 40:
        pygame.draw.rect(screen, color_light2, [width / 2.5, height / 4, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark2, [width / 2.5, height / 4, 140, 40])

        # superimposing the text onto our button
    screen.blit(text, (width / 2.5 + 37, height / 3))
    screen.blit(play, (width / 2.5 + 47, height / 6))
    screen.blit(ab, (width / 2.5 + 14, height / 4))

    # updates the frames of the game
    pygame.display.update()