import pygame 
import random
import math
from pygame import mixer
#assets : flaticon.com -> 2D icon assets 
#initialization of pygame

pygame.init()
 # creates screen and defines width and height
screen = pygame.display.set_mode((800, 600)) # size in pixels

#background 
background = pygame.image.load('background.png')

#background sound 
mixer.music.load('background.wav')
mixer.music.play(-1)
#title and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
# to make multiple enemies we will make a list of coordinate variables 
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):	
	enemyImg.append(pygame.image.load('enemy.png'))
	enemyX.append(random.randint(20, 700))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(10)
	enemyY_change.append(20)

#bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0, 800)
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state='ready'

# scoring
score_value=0
font = pygame.font.Font('test.otf', 32)

textX= 10
textY= 10


#game over text fucntion 
game_over= pygame.font.Font('test.otf', 100)

def game_over_text():
	over_text = font.render('GAME OVER' +str(score_value), True, (255, 255, 255))
	screen.blit(over_text, (200, 250))
def show_score(x,y):
	score = font.render('Score:' +str(score_value), True, (255, 255, 255))
	screen.blit(score, (x, y))

def bullet(x, y):
	global bullet_state
	bullet_state = 'fire'
	screen.blit(bulletImg, (x + 16, y + 10))

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, i):
	screen.blit(enemyImg[i], (x, y))
score= 0

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
	if distance <27:
		return True
	else:
		return False

#make a game loop
#anything will have to be here
running = True
while running:
	screen.fill((0,0,50))
	#adding a background, loading the background slows down the loop
	background = pygame.image.load('background.png')
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#if keystroke is performed check whether it's right or left
		if event.type == pygame.KEYDOWN: # push the key DOWN
			
			if event.key == pygame.K_LEFT:
				playerX_change = -5
			if event.key == pygame.K_RIGHT: 
				playerX_change = 5
			if event.key == pygame.K_SPACE: 

				if bullet_state is 'ready':
				 # bullet_Sound = mixer.Sound('laser.wav')
				 # bullet_Sound.play()
				 bulletX =playerX
				 bullet(bulletX, bulletY)
		if event.type == pygame.KEYUP: # release the button
			if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
				
				playerX_change = 0 # releasing the button changes the 'movement' speed down to zero

	#screen filled with RGB
	
	playerX += playerX_change
	
	#define the shape boundaries
	if playerX <=0:
		playerX =0
	elif playerX >=736:
		playerX = 736
	#enemy boundary collision and movement down
	for i in range(num_of_enemies):
		#GAME OVER
		if enemyY[i]> 440:
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <=0:
			enemyX_change[i] *= -1 # reverses direction 
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] *= -1
			enemyY[i] += enemyY_change[i]
		collision =isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision: 
			# explosion_Sound = mixer.Sound('explosion.wav')
			# explosion_Sound.play()
			bulletY=480
			bullet_state= 'ready'
			score_value += 1
		#return enemy to start position
			enemyX[i] = random.randint(20, 700)
			enemyY[i] = random.randint(50, 150)

			
		enemy(enemyX[i], enemyY[i], i)
		#bullet movement 
	if bulletY <=0 : 
		bulletY = 480
		bullet_state= 'ready'
	if bullet_state is 'fire':
		bullet(bulletX, bulletY)
		bulletY -= bulletY_change




	

	#call the player function 
	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()