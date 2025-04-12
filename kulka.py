import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("images/ball.png")
        self.zresetuj_pozycje()
        self.r = 16
        self.przegrana = False






    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        