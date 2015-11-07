import pygame, sys

pygame.init()

DISPLAY = (1366,768)
DEPTH = 32
FLAGS = 0

screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

while True:

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()

