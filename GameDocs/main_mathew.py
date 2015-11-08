import pygame, sys, time



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0


class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.index = 0
		self.playerSprites = []
		self.image1 = pygame.image.load("C:\Users\\frank\\Documents\\GitHub\\propituous-kidney\\GameDocs\\sprite animation\\move1.png")
		self.image1 = pygame.transform.scale(self.image1, (100,100))
		self.image2 = pygame.image.load("C:\Users\\frank\\Documents\\GitHub\\propituous-kidney\\GameDocs\\sprite animation\\move2.png")
		self.image2 = pygame.transform.scale(self.image2, (100,100))
		self.image3 = pygame.image.load("C:\Users\\frank\\Documents\\GitHub\\propituous-kidney\\GameDocs\\sprite animation\\move3.png")
		self.image3 = pygame.transform.scale(self.image3, (100,100))
		self.image4 = pygame.image.load("C:\Users\\frank\\Documents\\GitHub\\propituous-kidney\\GameDocs\\sprite animation\\move4.png")
		self.image4 = pygame.transform.scale(self.image4, (100,100))
		self.playerSprites.append(self.image1)
		self.playerSprites.append(self.image2)
		self.playerSprites.append(self.image3)
		self.playerSprites.append(self.image4)
		self.curImage = self.playerSprites[self.index]

	def update(self):
		self.index = self.index + 1
		if(self.index == 4):
			self.index = 0
		self.curImage = self.playerSprites[self.index]


def main():
	pygame.init()

	#-Variables
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot")
	screen.fill((0,255,255))

	new_sprite = Player()
	sprites = pygame.sprite.Group()

	while True:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		new_sprite.update()
		screen.blit(new_sprite.curImage, (0,HEIGHT/3*2-100))
		#sprites.draw(screen)
		pygame.display.flip()
		time.sleep(0.1)
		screen.fill((0,255,255))

main()