import pygame, sys



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0


def main():
	pygame.init()

	#-Variables
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()

	while True:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()

main()

