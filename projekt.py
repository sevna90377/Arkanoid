import pygame
from platforma import Platforma
from kulka import Kulka

pygame.init()
pygame.font.init()

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
zycia = 3

czcionka = pygame.font.SysFont('Calibri', 24)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')

platforma = Platforma()
kulka = Kulka()

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.poruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.poruszaj_platforma(1)

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()
    
    if kulka.przegrana:
        zycia -= 1
        if zycia <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)
    
    tekst = czcionka.render(f'Życia: {zycia}', False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
