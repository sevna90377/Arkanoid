import pygame

SZEROKOSC_EKRANU = 1024 
WYSOKOSC_EKRANU = 800

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("images/pad.png")
        self.porusza_sie = 0
        self.zresetuj_pozycje()

    #resetowanie pozycji
    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(SZEROKOSC_EKRANU/2-70, WYSOKOSC_EKRANU-100, 140, 30)

    #poruszanie platformą
    def ruszaj_platforma(self, wartosc):
        predkosc = 10
        self.rect.move_ip(wartosc*predkosc, 0)
        self.porusza_sie = wartosc
        if self.rect.left <= 0: self.rect.x = 0
        if self.rect.right >= SZEROKOSC_EKRANU: self.rect.x = SZEROKOSC_EKRANU-140
    
    #aktualizacja
    def aktualizuj(self):
        self.porusza_sie = 0