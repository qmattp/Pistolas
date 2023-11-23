import pygame, random

color= (255,255,255)
BLACK = (0, 0, 0)



class Calaveras(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

class Pistola(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Pistola.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x):
		self.speed_x += x

	def update(self):
		self.rect.x += self.speed_x
		player.rect.y = 510

class Bala(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Bala.png").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 4


pygame.init()

pygame.mixer.music.load("./Rickrolleaopa.wav")
pygame.mixer.music.play()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = pygame.image.load("Viejooeste.jpg").convert()
clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(50):
	meteor = Calaveras()
	meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)
	meteor.rect.y = random.randrange(450) 

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

player = Pistola()
all_sprite_list.add(player)
sound = pygame.mixer.Sound("./Disparo.wav")

 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
        

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(3)
			if event.key == pygame.K_SPACE:
				laser = Bala()
				laser.rect.x = player.rect.x + 45
				laser.rect.y = player.rect.y - 20

				laser_list.add(laser)
				all_sprite_list.add(laser)
				sound.play()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-3)


	all_sprite_list.update() 

	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)	
		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			
			score += 1
			print(score)

		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
    
   

	screen.blit(background, [0, 0])

	all_sprite_list.draw(screen)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()