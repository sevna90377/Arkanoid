import pygame
import random

SZEROKOSC_EKRANU = 1024 
WYSOKOSC_EKRANU = 800
vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.obraz = pygame.image.load("images/ball.png")
        self.zresetuj_pozycje()
        self.r = 16
        self.przegrana = False

    #resetowanie pozycji
    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU-140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    
    #aktualizacja
    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki)

    #sprawdz wszystkie mozliwe kolizje
    def sprawdz_kolizje(self, platforma, klocki):
        #krawedzie ekranu
        if self.rect.x <= 0: 
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1
        if self.rect.top <= 0:
            self.wektor.y *= -1
        if self.rect.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True

        #kolizja z platforma
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            self.wektor.x += platforma.porusza_sie*5
            if self.wektor.x < -10: self.wektor.x = -10
            if self.wektor.x > 10: self.wektor.x = 10

        #kolizja z klockami
        for klocek in klocki:
            #nastapila kolizja
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()
                break

    #metoda pomocnicza do kolizji z klockiem
    def kolizja_z_klockiem(self, kulka, klocek):
        dystans_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystans_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h / 2

        if dystans_x < kulka.r and dystans_y < kulka.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True
        return False