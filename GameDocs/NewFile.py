import pygame, sys



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0


def main():
	pygame.init()

	#-Variable4
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()
	pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))

	while True:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()

main()





