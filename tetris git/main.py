import pygame
import pygame.locals
pygame.init()


#variabili display
win = pygame.display.set_mode((500,650))
pygame.display.set_caption("tetris")

campo = [0] *200
#funzioni
def griglia():
    for a in range (10):
        for b in range (20):
            if campo [a + (b * 10)] == 1:
                print("aas")
                
            else:
                print("saasfasfas")
                pygame.draw.rect(win, bianco , (20+(a*20),40+(b*20),20,20), 1)
                
#loop
def giocoFunzione():
    inFunzione = True
    print (inFunzione)
    while inFunzione == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inFunzione = False
                
        print("saccodimerda")
    pygame.quit()
    quit()
        
    
#colori
rosso = (255,0,0)
bianco = (0,255,255)

    
    
#campo
griglia()
pygame.draw.line (win, rosso, (20,40), (20,440), 2)
pygame.draw.line (win, rosso, (20,440), (220,440), 2)
pygame.draw.line (win, rosso, (220,40), (220,440), 2)
pygame.display.update()
giocoFunzione()



