#submarine.py
import pygame
import os

WIDTH = 1000
HEIGHT = 800
FPS = 30

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (22, 115, 28)

#Initialize PyGame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Tank')
clock = pygame.time.Clock()

##### Create The Tank #####
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Tank(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((25,25))
		tank_img = os.path.join(img_folder,'Tank_small.png')

		self.image = pygame.image.load(tank_img).convert()
		#self.image.set_colorkey(RED)

		#self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/3
		self.rect.bottom = HEIGHT - 0

		self.speedx = 0
		self.speedy = 0

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5

		if keystate[pygame.K_RIGHT]:
			self.speedx = 5

		if keystate[pygame.K_UP]:
			self.speedy = -5

		if keystate[pygame.K_DOWN]:
			self.speedy = 5

		self.rect.x += self.speedx

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH

		if self.rect.left < 0:
			self.rect.left = 0

		self.rect.y += self.speedy

		if self.rect.top > HEIGHT:
			self.rect.top = HEIGHT

		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT

		if self.rect.bottom < 0:
			self.rect.bottom = 0



# Player call is sprite
all_sprites = pygame.sprite.Group()
tank = Tank()
all_sprites.add(tank)






running = True

while running:
	clock.tick(FPS)

	for event in pygame.event.get():
		#check for close game
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()
