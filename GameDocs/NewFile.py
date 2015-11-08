import pygame, sys, random



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0
BLACK = (0,0,0)
counter = 0 


class Rectangle(pygame.sprite.Sprite):
	def __init__(self, w, h, screens, counter):
		random_x = random.randint(WIDTH/2, 1366)
		random_y = random.randint(HEIGHT/3, 768/2)
		self.newRect = pygame.draw.rect(screens, BLACK, (random_x, random_y, 100, 150))


		
		

def main():
	pygame.init()
	counter = 0
	#-Variable4
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()
	a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
	

	while counter<=1:
		b = Rectangle(100, 100, screen, counter)
		counter = counter + 1

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

main()





