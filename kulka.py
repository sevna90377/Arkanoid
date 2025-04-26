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
        self.sprawdz_kolizje(platforma)

    def sprawdz_kolizje(self, platforma):
        
        # krawędzie ekranu
        if self.rect.x <= 0 or self.rect.right >= SZEROKOSC_EKRANU:
            self.predkosc.x *= -1
        if self.rect.y <=0:
            self.predkosc.y *= -1
        if self.rect.y >= WYSOKOSC_EKRANU:
            self.przegrana = True

        # platforma
        if self.rect.colliderect(platforma.rect):
            self.predkosc.y *= -1
            self.predkosc.x += platforma.porusza_sie * 5
            if self.predkosc.x > 10: 
                self.predkosc.x = 10
            if self.predkosc.x < -10:
                self.predkosc.x = -10

