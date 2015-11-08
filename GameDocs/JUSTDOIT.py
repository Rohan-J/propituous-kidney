import pygame, sys, time, os, random
pygame.init()

pygame.mixer.music.load("NitroFun_NewGame.ogg")
pygame.mixer.music.play(-1)

#-Constants
WIDTH = 1366
HEIGHT = 768
DISPLAY = (WIDTH,HEIGHT)
DEPTH = 32
FLAGS = 0
BLACK = (0, 0, 0)
Screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

#global var + rohand's stufff
jumpFlag = False
score=0
black=(100,149,237)
end_it=False
background_image = pygame.image.load("tilepatterns_DSC9320b.jpg").convert()
while (end_it==False):
    Screen.blit(background_image,[0,0])
    font = pygame.font.SysFont("Ariel", 42)
    nlabel=font.render("Welcome! Click to Play!", 1, (0, 0, 0))
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		pygame.quit()
    		sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            end_it=True
    Screen.blit(nlabel,[500,384])
    pygame.display.flip()


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.xc = x
		self.yc = y
		self.cony = y
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
		self.rect = self.image1.get_rect()
		self.playerSprites.append(self.image1)
		self.playerSprites.append(self.image2)
		self.playerSprites.append(self.image3)
		self.playerSprites.append(self.image4)
		self.curImage = self.playerSprites[self.index]


	def jump(self):
		self.jumps = True

	def update(self):
		global jumpFlag
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
			if(self.yc < HEIGHT/3*2-100):
				self.yc = self.yc + self.changeY2
				self.changeY2 += 0.35
			else:
				self.fall = True
				jumpFlag = False
				self.yc = HEIGHT/3*2-100
				self.changeY2 = 0

		if(self.count == 5):
			self.index = self.index + 1
			if(self.index == 4):
				self.index = 0
			self.count = 0
		self.count = self.count + 1
		if(self.jumps != True and self.fall == True):
			self.curImage = self.playerSprites[self.index]

class Rectangle(pygame.sprite.Sprite):
	def __init__(self, w, h, screens):
		pygame.sprite.Sprite.__init__(self)
		self.counter = 0
		self.random_x = random.randint(100, 150)
		self.random_y = random.randint(100, 350)
		self.inOut = random.randint(1,2)
		self.fadeCount = 0
		if(self.inOut == 1):
			self.opacity = 255
		elif(self.inOut == 2):
			self.opacity = 1
		if(self.random_x > 200):
			self.random_y = 140
		self.image = pygame.Surface([self.random_x, self.random_y])
		self.rect = self.image.get_rect()
		self.y = self.random_y
		self.image.fill(BLACK)
		self.selfscreen = screens
		self.xv = WIDTH


	def update(self):
		if(self.xv > 0-self.random_x):
			self.image.set_alpha(self.opacity)
			self.selfscreen.blit(self.image,(self.xv, HEIGHT/3))
			self.xv = self.xv - 10
			if(self.inOut == 1):
				self.opacity = self.opacity - 3
			elif(self.inOut == 2):
				if(self.fadeCount >= 60):
					self.opacity = self.opacity + 2
				self.fadeCount += 1
		else:
			self.kill()


def gameOver():
	global score
	font = pygame.font.Font(None, 36)
	clicked = False
	endScore = font.render("Final Score: " + str(score), True, BLACK)
	endScore_rect = endScore.get_rect()
	endScore_x= WIDTH/2 - endScore_rect.width/2
	text = font.render("Game Over! Click to exit.", True, BLACK)
	text_rect = text.get_rect()
	text_x = WIDTH/2 - text_rect.width/2
	text_y = HEIGHT/2 - text_rect.height/2
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	background_image = pygame.image.load("tilepatterns_DSC9320b.jpg").convert()
	screen.fill((0,255,255))
	while(not clicked):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				clicked = True
		screen.blit(text, [text_x, text_y])
		screen.blit(endScore, [text_x, 300])
		pygame.display.flip()
		screen.blit(background_image,[0,0])


def main():

	lives = 3
	done = False
	global score
	global jumpFlag
	pygame.init()
	collided = False
	clock = pygame.time.Clock()
	font = pygame.font.Font(None,36)
	rate = 0
	definedRate = 120
	limit = 0
	upgrade = 0

	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("Run")
	screen.fill((0,255,255))

	new_sprite = Player(0, HEIGHT/3*2-100)
	sprites = pygame.sprite.Group()
	blocks = pygame.sprite.Group()
	a = Rectangle(100, 100, screen)
	sprites.add(a)
	sprites.add(new_sprite)
	blocks.add(a)
	background_image = pygame.image.load("tilepatterns_DSC9320b.jpg").convert()


	while not done:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if(jumpFlag == False):
						jumpFlag = True
						new_sprite.changeY1 = 15
						new_sprite.changeY2 = 6
						new_sprite.jump()

		for x in blocks:
			if(new_sprite.yc > x.y and x.xv <= 100 and limit > 60):
				if(HEIGHT/3-x.y > 100):
					pass
				else:
					print("You crashed")
					limit = 0
					lives = lives - 1
					if(lives == 0):
						done = True



		if(rate == definedRate): #150
			if(upgrade == 10):
				definedRate = definedRate - 15
				upgrade = 0
			a = Rectangle(100, 100, screen)
			sprites.add(a)
			blocks.add(a)
			#print(HEIGHT/3*1-a.y-100)
			rate = 0
			upgrade = upgrade + 1


		livesText = font.render("Lives: " + str(lives), True, BLACK)
		lives_rect = livesText.get_rect()
		scoreText = font.render("Score: " + str(score), True, BLACK)
		score_rect = scoreText.get_rect()
		#new_sprite.checkCollision(new_sprite, blocks)
		a = pygame.draw.rect(screen, (0,0,0), (0,HEIGHT/3*2,1366,384))
		sprites.update()
		screen.blit(new_sprite.curImage, (new_sprite.xc, new_sprite.yc))
		screen.blit(livesText, [WIDTH-200, 50])
		screen.blit(scoreText, [10, 50])
			#sys.exit()
		rate = rate + 1
		limit = limit + 1
		score = score + 1
		pygame.display.flip()
		clock.tick(60)
		screen.blit(background_image,[0,0])
main()
gameOver()