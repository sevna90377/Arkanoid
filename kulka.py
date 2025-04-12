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


    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.predkosc = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.predkosc.rotate_ip(self.kat_nachylenia)
        self.przegrana = False

    def aktualizuj(self, platforma):
        self.wspolrzedne += self.predkosc
        self.rect.center = self.wspolrzedne

    def sprawdz_kolicje(self, platform):
        
        # krawędzie ekranu
        if self.rect.x <= 0 or self.rect.right >= SZEROKOSC_EKRANU:
            self.predkosc.x *= -1

