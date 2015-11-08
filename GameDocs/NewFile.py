import pygame, sys, random



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0
BLACK = (0,0,0)


class Rectangle(pygame.sprite.Sprite):
	def __init__(self, w, h, screens):
		self.newRect = pygame.draw.rect(screens, BLACK, (1300, 384, w, h))
		

		
		

def main():
	pygame.init()

	#-Variable4
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()
	a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
	

	while True:
		b = Rectangle(100, 100, screen)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()

main()





