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
		self.random_x = random.randint(WIDTH/2, 1366)
		self.random_y = random.randint(HEIGHT/3, 768/2)
		self.newRect = pygame.draw.rect(screens, BLACK, (self.random_x, self.random_y, 100, 150))

	def update(self):
		self.newRect.move(self.random_x - 1, self.random_y)
		print self.random_x - 1
		print self.random_y
		self.random_x = self.random_x - 1


		
		

def main():
	pygame.init()
	counter = 0
	#-Variable4
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))
	sprites = pygame.sprite.Group()
	a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
	

	while counter<=2:
		b = Rectangle(100, 100, screen, counter) 
		counter = counter +2
		pygame.display.update()
		b.update()
		
		print ('hello')
	

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()
		clock.tick()

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

main()





