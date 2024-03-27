import pygame
import time

from pygame.locals import*
from time import sleep

from abc import ABC, abstractmethod
class Sprite(ABC):
	def	__init__(self, xPos, yPos, width, height, im):
		self.x = xPos
		self.y = yPos
		self.w = width
		self.h = height
		self.image = pygame.image.load(im)
	
	def printsprite(self):
		print(self.x,self.y,self.w,self.h)

	def draw(self, screen, scrollPosX, scrollPosY):
		LOCATION = (self.x - scrollPosX, self.y - scrollPosY)
		SIZE = (self.w, self.h)
		screen.blit(pygame.transform.scale(self.image,SIZE),LOCATION)

	def isTile(self):
		return False
	
	def isLink(self):
		return False
	
	def isPot(self):
		return False
	
	def isBoomerang(self):
		return False
		
	

class Tile(Sprite):
	def __init__(self,xPos,yPos):
		super().__init__(xPos,yPos,50,50,"tile.jpg")
		# self.x = xPos
		# self.y = yPos
		# self.h = 50
		# self.w = 50
		self.isValid = True
		#self.image = pygame.image.load("tile.jpg")

	def update(self):
		return self.isValid
	
	def isTile(self):
		return True
	
class Pot(Sprite):
	def __init__(self,xPos,yPos):
		super().__init__(xPos,yPos,35,35,"pot.png")
		self.images = []
		self.imagenum = 0
		self.speed = 5
		self.xdirection = 0
		self.ydirection = 0
		self.time = 100
		self.isValid = True
		self.broken = False
		for i in range(2):
			if(i == 0):
				self.images.append(pygame.image.load("pot.png"))
			elif(i == 1):
				self.images.append(pygame.image.load("pot_broken.png"))
	
	def draw(self, screen, scrollPosX,scrollPosY):
		LOCATION = (self.x - scrollPosX, self.y - scrollPosY)
		SIZE = (self.w, self.h)
		screen.blit(pygame.transform.scale(self.images[self.imagenum],SIZE),LOCATION)

	def potUpdateImgNum(self):
		if(self.broken == True):
			self.imagenum = 1
		elif(self.broken == False):
			self.imagenum = 0

	def update(self):
		self.x += self.speed * self.xdirection
		self.y += self.speed * self.ydirection
		if(self.broken == True):
			self.time -= 1
			if(self.time == 0):
				self.isValid = False
				#print(self.isValid)
		return self.isValid

	def Break(self):
		self.broken = True

	def isPot(self):
		return True
	
class Boomerang(Sprite):
	def __init__(self,xPos,yPos):
		super().__init__(xPos,yPos,20,20,"boomerang1.png")
		self.thrown = True
		self.direction = 0
		self.canPass = False

	def update(self):
		if(self.direction == 0):
			self.y += 5
		if(self.direction == 1):
			self.x += 5
		if(self.direction == 2):
			self.x -= 5
		if(self.direction == 3):
			self.y -= 5
		if(self.thrown == False):
			return False
		return True

	def isBoomerang(self):
		return True
	
	def move(self):
		if(self.direction == 0):
			self.y += 5
		if(self.direction == 1):
			self.x += 5
		if(self.direction == 2):
			self.x -= 5
		if(self.direction == 3):
			self.y -= 5
	
class Link(Sprite):
	def __init__(self,xPos,yPos):
		super().__init__(xPos,yPos,50,50,"link1.png")
		self.images = []
		self.imagenum = 0
		self.direction = 0
		self.previousX = 0
		self.previousY = 0
		self.walkin = False
		for i in range(50):
			self.images.append(pygame.image.load("link" + str(i + 1) + ".png"))
			
		#print(self.images[1])


	def draw(self, screen, scrollPosX,scrollPosY):
		LOCATION = (self.x - scrollPosX, self.y - scrollPosY)
		SIZE = (self.w, self.h)
		screen.blit(pygame.transform.scale(self.images[self.imagenum],SIZE),LOCATION)

	def updateImgNum(self):
		if(self.direction == 0): #down
			#print('true!')
			if(self.imagenum > 11):
				self.imagenum = 0
			self.imagenum += 1
		if(self.direction == 2): #left
			if(self.imagenum < 13 or self.imagenum > 24):
				self.imagenum = 13
			self.imagenum += 1
		if(self.direction == 1): #right
			if(self.imagenum < 26 or self.imagenum  > 37):
				self.imagenum = 26
			self.imagenum += 1
		if(self.direction == 3): #up
			if(self.imagenum < 39 or self.imagenum > 48):
				self.imagenum = 39
			self.imagenum += 1

	def update(self):
		return True
	
	def isLink(self):
		return True


class Model():
	def __init__(self):
		self.dest_x = 0
		self.dest_y = 0
		self.sprites = []
		self.thrown = False
		self.link = Link(70,70)
		self.sprites.append(Tile(0,0))
		self.sprites.append(Tile(50,0))
		self.sprites.append(Tile(100,0))
		self.sprites.append(Tile(150,0))
		self.sprites.append(Tile(200,0))
		self.sprites.append(Tile(250,0))
		self.sprites.append(Tile(300,0))
		self.sprites.append(Tile(350,0))
		self.sprites.append(Tile(400,0))
		self.sprites.append(Tile(450,0))
		self.sprites.append(Tile(0,50))
		self.sprites.append(Tile(0,100))
		self.sprites.append(Tile(0,150))
		self.sprites.append(Tile(0,200))
		self.sprites.append(Tile(0,250))
		self.sprites.append(Tile(0,300))
		self.sprites.append(Tile(0,350))
		self.sprites.append(Tile(0,400))
		self.sprites.append(Tile(0,450))
		self.sprites.append(Tile(0,500))
		self.sprites.append(Tile(0,550))
		self.sprites.append(Tile(0,600))
		self.sprites.append(Tile(0,650))
		self.sprites.append(Tile(0,700))
		self.sprites.append(Tile(0,750))
		self.sprites.append(Tile(0,800))
		self.sprites.append(Tile(0,850))
		self.sprites.append(Tile(0,900))
		self.sprites.append(Tile(0,950))
		self.sprites.append(Tile(50,950))
		self.sprites.append(Tile(100,950))
		self.sprites.append(Tile(150,950))
		self.sprites.append(Tile(200,950))
		self.sprites.append(Tile(250,950))
		self.sprites.append(Tile(300,950))
		self.sprites.append(Tile(350,950))
		self.sprites.append(Tile(400,950))
		self.sprites.append(Tile(450,950))
		self.sprites.append(Tile(500,950))
		self.sprites.append(Tile(550,950))
		self.sprites.append(Tile(600,950))
		self.sprites.append(Tile(650,950))
		self.sprites.append(Tile(700,950))
		self.sprites.append(Tile(750,950))
		self.sprites.append(Tile(800,950))
		self.sprites.append(Tile(850,950))
		self.sprites.append(Tile(900,950))
		self.sprites.append(Tile(950,950))
		self.sprites.append(Tile(950,900))
		self.sprites.append(Tile(950,850))
		self.sprites.append(Tile(950,800))
		self.sprites.append(Tile(950,750))
		self.sprites.append(Tile(950,700))
		self.sprites.append(Tile(950,650))
		self.sprites.append(Tile(950,600))
		self.sprites.append(Tile(950,550))
		self.sprites.append(Tile(950,500))
		self.sprites.append(Tile(950,450))
		self.sprites.append(Tile(950,400))
		self.sprites.append(Tile(950,350))
		self.sprites.append(Tile(950,300))
		self.sprites.append(Tile(950,250))
		self.sprites.append(Tile(950,200))
		self.sprites.append(Tile(950,150))
		self.sprites.append(Tile(950,100))
		self.sprites.append(Tile(950,50))
		self.sprites.append(Tile(950,0))
		self.sprites.append(Tile(900,0))
		self.sprites.append(Tile(850,0))
		self.sprites.append(Tile(800,0))
		self.sprites.append(Tile(750,0))
		self.sprites.append(Tile(700,0))
		self.sprites.append(Tile(650,0))
		self.sprites.append(Tile(600,0))
		self.sprites.append(Tile(550,0))
		self.sprites.append(Tile(500,0))
		#self.sprites.append(Tile(300,200))
		self.sprites.append(self.link)
		#self.pot = Pot(200,200)
		self.sprites.append(Pot(200,200))
		self.sprites.append(Pot(400,300))
		self.sprites.append(Pot(250,350))
		self.sprites.append(Tile(50,300))
		self.sprites.append(Tile(100,300))
		self.sprites.append(Tile(150,300))
		self.sprites.append(Tile(50,450))
		self.sprites.append(Tile(100,450))
		self.sprites.append(Tile(150,450))
		self.sprites.append(Tile(200,450))
		self.sprites.append(Tile(400,450))
		self.sprites.append(Tile(450,450))
		self.sprites.append(Tile(450,50))
		self.sprites.append(Tile(450,100))
		self.sprites.append(Tile(450,150))
		self.sprites.append(Tile(450,400))
		self.sprites.append(Tile(450,200))
		self.sprites.append(Tile(500,50))
		self.sprites.append(Tile(500,100))
		self.sprites.append(Tile(500,150))
		self.sprites.append(Tile(500,400))
		self.sprites.append(Tile(500,200))
		self.sprites.append(Tile(500,450))
		self.sprites.append(Tile(550,450))
		self.sprites.append(Tile(600,450))
		self.sprites.append(Tile(650,450))
		self.sprites.append(Tile(700,450))
		self.sprites.append(Tile(900,450))
		self.sprites.append(Tile(950,450))
		self.sprites.append(Tile(500,500))
		self.sprites.append(Tile(550,500))
		self.sprites.append(Tile(600,500))
		self.sprites.append(Tile(650,500))
		self.sprites.append(Tile(700,500))
		self.sprites.append(Tile(900,500))
		self.sprites.append(Tile(950,500))
		self.sprites.append(Tile(500,550))
		self.sprites.append(Tile(500,600))
		self.sprites.append(Tile(500,650))
		self.sprites.append(Tile(500,700))
		self.sprites.append(Tile(500,900))
		self.sprites.append(Tile(450,500))
		self.sprites.append(Tile(450,550))
		self.sprites.append(Tile(450,600))
		self.sprites.append(Tile(450,650))
		self.sprites.append(Tile(450,700))
		self.sprites.append(Tile(450,900))
		self.sprites.append(Tile(450,950))
		self.sprites.append(Tile(50,500))
		self.sprites.append(Tile(100,500))
		self.sprites.append(Tile(150,500))
		self.sprites.append(Tile(200,500))
		self.sprites.append(Tile(400,500))
		self.sprites.append(Tile(50,650))
		self.sprites.append(Tile(100,650))
		self.sprites.append(Tile(150,650))
		self.sprites.append(Tile(300,800))
		self.sprites.append(Tile(250,800))
		self.sprites.append(Pot(150,800))
		self.sprites.append(Pot(150,850))
		self.sprites.append(Tile(550,700))
		self.sprites.append(Tile(600,700))
		self.sprites.append(Tile(650,700))
		self.sprites.append(Tile(800,850))
		self.sprites.append(Tile(800,900))
		self.sprites.append(Tile(800,950))
		self.sprites.append(Pot(800,600))
		self.sprites.append(Pot(500,500))
		self.sprites.append(Pot(600,600))
		self.sprites.append(Tile(550,200))
		self.sprites.append(Tile(600,200))
		self.sprites.append(Tile(750,300))
		self.sprites.append(Tile(800,200))
		self.sprites.append(Pot(600, 350))
		self.sprites.append(Pot(650,100))
		#self.sprites.append(Pot(550,350))
		#self.sprites.append(Tile(500,900))
		
		#vector = np.array(self.sprites)

	def addRang(self, link):
		self.x = link.x
		self.y = link.y
		self.d = link.direction
		self.boomerang = Boomerang(link.x, link.y)
		self.boomerang.direction = link.direction
		self.sprites.append(self.boomerang)

	def detectCollision(self, sprite1,sprite2):
		if(sprite1.x + sprite1.w < sprite2.x):
			return False
		if(sprite1.x > sprite2.x + sprite2.w):
			return False
		if(sprite1.y + sprite1.h < sprite2.y):
			return False
		if(sprite1.y > sprite2.y + sprite2.h):
			return False
		return True

	def update(self):
		for i in self.sprites:
			if(i.update() == False):
				self.sprites.remove(i)
			for j in self.sprites:
				if(self.detectCollision(i,j)):
					if(i.isLink() and j.isTile()):
						self.link.x = self.link.previousX
						self.link.y = self.link.previousY
					if(i.isPot() and j.isBoomerang()):
						if(i.broken == True):
							j.canPass = True
						else:
							i.broken = True
							i.potUpdateImgNum()
							j.thrown = False
							self.sprites.remove(j)
					if(i.isPot() and j.isTile()):
						i.speed = 0
						i.broken = True
						i.potUpdateImgNum()
					if(i.isBoomerang() and j.isTile()):
						i.thrown = False
					if(i.isLink() and j.isPot()):
						if(j.broken == True):
							self.link.walkin = True
						else:
							self.link.x = self.link.previousX
							self.link.y = self.link.previousY
							j.broken = True
							if(self.link.direction == 0):
								j.ydirection = 1
							if(self.link.direction == 1):
								j.xdirection = 1
							if(self.link.direction == 2):
								j.xdirection = -1
							if(self.link.direction == 3):
								j.ydirection = -1

	def set_dest(self, pos):
		self.dest_x = pos[0]
		self.dest_y = pos[1]

class View():
	def __init__(self, model):
		screen_size = (500,500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.turtle_image = pygame.image.load("tile.jpg")
		self.model = model
		self.model.rect = self.turtle_image.get_rect()
		self.xPos = 0
		self.yPos = 0
	def update(self):
		self.screen.fill([0,200,100])
		for sprite in self.model.sprites:
			sprite.draw(self.screen, self.xPos,self.yPos)
		if(self.model.link.x > 500):
			self.xPos += 500
		if(self.model.link.x < self.xPos):
			self.xPos -= 500
		if(self.model.link.y > 500):
			self.yPos += 500
		if(self.model.link.y < self.yPos):
			self.yPos -= 500
		pygame.display.flip()

	def setscrollPosX(self,X):
		if(X > self.xPos + 500):
			self.xPos += 500
		elif(X < self.xPos):
			self.xPos -= 500
	
	def setscrollPosY(self,Y):
		if(Y > self.yPos + 500):
			self.yPos += 500
		elif(Y < self.yPos):
			self.yPos -= 500

class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True
		self.thrown = False
		self.numrangs = 0
		self.control = False

	def update(self):
		self.model.link.previousX = self.model.link.x
		self.model.link.previousY = self.model.link.y
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
			elif event.type == KEYUP:
				if(event.key == K_LCTRL):
					self.control = True
					self.model.addRang(self.model.link)
		keys = pygame.key.get_pressed()
		if keys[K_DOWN]:
			self.model.link.y += 5
			self.model.link.direction = 0
			self.model.link.updateImgNum()
		if keys[K_LEFT]:
			self.model.link.x -= 5
			self.model.link.direction = 2
			self.model.link.updateImgNum()
		if keys[K_RIGHT]:
			self.model.link.x += 5
			self.model.link.direction = 1
			self.model.link.updateImgNum()
		if keys[K_UP]:
			self.model.link.y -= 5
			self.model.link.direction = 3
			self.model.link.updateImgNum()
		

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")