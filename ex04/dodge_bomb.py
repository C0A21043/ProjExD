import pygame as pg 
import sys

def main():
    clock=pg.time.Clock()
    

    
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc=pg.display.set_mode((1600,900)) #Surface
    soto_sfc=pg.image.load("fig/pg_bg.jpg")
    soto_rct=soto_sfc.get_rect()
    
    while True:
        scrn_sfc.blit(soto_sfc,soto_rct)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            pg.display.update()
            clock.tick(1000)
    
    


if __name__== "__main__":
    main()
    pg.init()
    pg.quit()
    sys.exit

