import pygame, sys, time, os



#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.xc = x
		self.yc = y
		self.fall = True
		self.changeY1 = 0
		self.changeY2 = 0
		self.jumps = False
		self.count = 0
		self.index = 0
		self.playerSprites = []
		self.image1 = pygame.image.load("move1.png")
		self.image1 = pygame.transform.scale(self.image1, (100,100))
		self.image2 = pygame.image.load("move2.png")
		self.image2 = pygame.transform.scale(self.image2, (100,100))
		self.image3 = pygame.image.load("move3.png")
		self.image3 = pygame.transform.scale(self.image3, (100,100))
		self.image4 = pygame.image.load("move4.png")
		self.image4 = pygame.transform.scale(self.image4, (100,100))
		self.playerSprites.append(self.image1)
		self.playerSprites.append(self.image2)
		self.playerSprites.append(self.image3)
		self.playerSprites.append(self.image4)
		self.curImage = self.playerSprites[self.index]


	def jump(self):
		self.jumps = True

	def update(self):
		if(self.jumps == True):
			self.curImage = self.playerSprites[1]
			self.yc = self.yc - self.changeY1 #asd
			self.changeY1 = self.changeY1 - 0.35
			if(self.changeY1 <= 0):
				self.changeY1 = 0
				self.jumps = False
		if(self.jumps == False):
			self.fall = False
			self.curImage = self.playerSprites[1]
			if(self.yc < HEIGHT/3*2-88):
				self.yc = self.yc + self.changeY2
				self.changeY2 += 0.35
			else:
				self.fall = True
				self.yc = HEIGHT/3*2-88
				self.changeY2 = 0

		if(self.count == 5):
			self.index = self.index + 1
			if(self.index == 4):
				self.index = 0
			self.count = 0
		self.count = self.count + 1
		if(self.jumps != True and self.fall == True):
			self.curImage = self.playerSprites[self.index]


def main():
	pygame.init()
	clock = pygame.time.Clock()
	#-Variables
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("rohan is hot, but rayyaan is hotter")
	screen.fill((0,255,255))

	new_sprite = Player(0, HEIGHT/3*2-88)
	sprites = pygame.sprite.Group()

	while True:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					new_sprite.changeY1 = 15
					new_sprite.changeY2 = 6
					new_sprite.jump()

		new_sprite.update()
		screen.blit(new_sprite.curImage, (new_sprite.xc, new_sprite.yc))
		a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
		pygame.display.flip()
		clock.tick(60)
		screen.fill((0,255,255))

main()