import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.image = pygame.image.load('images/buleton.png')
        self.rect = self.image.get_rect()
        self.color = (229, 230,25)
        self.speed = 3.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю на экране"""
        self.screen.blit(self.image, self.rect)