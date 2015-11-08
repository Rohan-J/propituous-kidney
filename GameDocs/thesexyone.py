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
	def __init__(self, w, h, screens):
		pygame.sprite.Sprite.__init__(self)
		self.counter = 0
		self.random_x = random.randint(100, 400)
		self.random_y = random.randint(100, 400)
		self.selfscreen = screens
		self.xv = WIDTH

	def update(self):
		self.newRect = pygame.draw.rect(self.selfscreen, BLACK, (self.xv, HEIGHT/3*1, self.random_x, self.random_y))
		self.xv = self.xv - 10


		
		

def main():
	pygame.init()
	#-Variable4
	clock = pygame.time.Clock()
	limit = 5
	rate = 0
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()
	sprites.add(Rectangle(100, 100, screen))

	while True:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
		if(rate == 200):
			sprites.add(Rectangle(100, 100, screen))
			rate = 0
		a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
		sprites.update()
		rate = rate + 1
		pygame.display.flip()
		clock.tick(60)
		screen.fill((0,255,255))


main()





