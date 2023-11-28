import pygame, random

color= (255,255,255)
BLACK = (0, 0, 0)
RED = (183, 20, 20)

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

class Calaveras(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Calavera.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1

		if self.rect.y > 600:
			self.rect.y = -20
			self.rect.x = random.randrange(900)

class Fuego(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("fuego.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

class Escopeta(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.imagea = pygame.image.load("Escopeta.png").convert()
		self.imagea.set_colorkey(BLACK)
		self.Velocidad_X = 0
		self.Velocidad_Y = 0
		self.rect2 = self.imagea.get_rect()
        

	def changespeed(self, x):
		self.Velocidad_X += x

	def update(self):
		self.rect.x += self.Velocidad_X
		player.rect.x = 600

	

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
		player.rect.y = 600

class Bala(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Bala.png").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 4 

class BalaEscopeta(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image2 = pygame.image.load("BalaEscopeta.png").convert()
		self.recta = self.image2.get_rect()

	def update(self):
		self.recta.y -= 4 

pygame.init()

pygame.mixer.music.load("./Rickrolleaopa.wav")
pygame.mixer.music.play()

fuente = pygame.font.Font(None, 60)

Posicionx=390
Posiciony=350

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = pygame.image.load("Viejooeste.jpg").convert()

clock = pygame.time.Clock()

done = False
global score 
score = 0


Fuego_a = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
Balat_list = pygame.sprite.Group()
Escopeta_list = pygame.sprite.Group()
BalatEscopeta_list = pygame.sprite.Group()

for i in range(78):
	meteor = Calaveras()
	meteor.rect.x = random.randrange(720)
	meteor.rect.y = random.randrange(350)

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

fuego= Fuego()
player = Pistola()
player2= Escopeta()
all_sprite_list.add(player)
Escopeta_list.add(player2)
sound = pygame.mixer.Sound("./Disparo.wav")
sound2 = pygame.mixer.Sound("./Disparo.wav")
 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
        
		if event.type == pygame.KEYDOWN:
			#Movimientos jugador 2
			if event.key == pygame.K_LEFT:
				player.changespeed(-3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(3)
		    #Movimientos jugador 2
			if event.key == pygame.K_a:
				player2.changespeed(-3)
			if event.key == pygame.K_d:
				player2.changespeed(3)

			if event.key == pygame.K_l:
				Balat2 = BalaEscopeta()
				Balat.rect.x = player.rect.x + 45
				Balat.rect.y = player.rect.y - 20
 
				Balat_list.add(Balat2)
				all_sprite_list.add(Balat2)
				sound.play()
			#Disparando jugador 1
			if event.key == pygame.K_SPACE:
				Balat = Bala()
				Balat.rect.x = player.rect.x + 45
				Balat.rect.y = player.rect.y - 20
 
				Balat_list.add(Balat)
				all_sprite_list.add(Balat)
				sound.play()
				Fuego_a.add(Balat)
            
            

		if event.type == pygame.KEYUP:
			#Movimientos de jugador1
			if event.key == pygame.K_LEFT:
				player.changespeed(3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-3)
			#Movimientos de jugador2
			if event.key == pygame.K_a:
				player2.changespeed(3)
			if event.key == pygame.K_d:
				player2.changespeed(-3)
			
            
        

         
	all_sprite_list.update() 

	for Balat in Balat_list:
		meteor_hit_list = pygame.sprite.spritecollide(Balat, meteor_list, True)	
		for meteor in meteor_hit_list:
			all_sprite_list.remove(Balat)
			Balat_list.remove(Balat)
			score += 1
			print(score)
            
		if Balat.rect.y < -10:
			all_sprite_list.remove(Balat)
			Balat_list.remove(Balat)
           
           
        
    
   

	screen.blit(background, [0, 0])

	all_sprite_list.draw(screen)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()