import pygame as pg 
import sys

def main():
    clock=pg.time.Clock()
    

    
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc=pg.display.set_mode((1600,900)) #Surface(scrn)
    soto_sfc=pg.image.load("fig/pg_bg.jpg")
    soto_rct=soto_sfc.get_rect()
    tori_sfc=pg.image.load("fig/3.png") #Surface(tori)
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400
    tori_sfc.blit(tori_sfc,tori_rct)#blit(tori)
    
    while True:
        scrn_sfc.blit(soto_sfc,soto_rct)#blit(soto)
        scrn_sfc.blit(tori_sfc,tori_rct)
        key_lst=pg.key.get_pressed()
        
        if key_lst[pg.K_UP]==True:
            tori_rct.centery-=1
        elif key_lst[pg.K_DOWN]==True:
            tori_rct.centery+=1
        elif key_lst[pg.K_LEFT]==True:
            tori_rct.centerx-=1
        elif key_lst[pg.K_RIGHT]==True:
            tori_rct.centerx+=1
        
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

