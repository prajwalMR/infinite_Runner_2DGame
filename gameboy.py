import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GAMEBOY')

black = (0,0,0)
white = (255,255,255)
blue = (0,191,255)

x = 50
y = 475

man_health = 100

high_score = 0

score = 0

cloud1_x = 800
cloud2_x = 1375

cloud1_y =  25
cloud2_y = 	150

fire1_x = 600
fire1_y = 475

cac_x = 800
cac_y = 465

bat_x = random.randrange(550,2050)
bat_y = 300



batCount = 1 

fireBall_x = x

toggle = 0

clock = pygame.time.Clock()
crashed = False
manImg = pygame.image.load('runner1.jpg')
groundImage = pygame.image.load('ground.gif')
cloudImage = pygame.image.load('cloud.jpg')
fireImage = pygame.image.load('fire.gif').convert_alpha()
cactus = pygame.image.load('bush.jpg')
cactus = pygame.transform.scale(cactus, (200, 100))
bat1 = pygame.image.load('bat1.png')
bat2 = pygame.image.load('bat2.png')
bat3 = pygame.image.load('bat3.png')

fire1_width = fireImage.get_size()[0]
fire1_height = fireImage.get_size()[1]

bat_width = bat3.get_size()[0]
bat_height = bat3.get_size()[0]

curBat = bat1

update_delay = 200

last_update = pygame.time.get_ticks()

frames = ('bat1.png' , 'bat2.png' , 'bat3.png')
fps = 60

bgColor = white

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    crashed = True
    exit()

def socre_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def man(x,y , manImg):
    gameDisplay.blit(manImg, (x,y))

def drawCloud(cloud_x , cloud_y):
	gameDisplay.blit(cloudImage , (cloud_x , cloud_y))

def drawFire():
	gameDisplay.blit(fireImage , (fire1_x , fire1_y))

def drawCactus():
	gameDisplay.blit(cactus , (cac_x , cac_y))

def fireBullet(fireBall_x , fireBall_y):
	gameDisplay.blit(fireBallImage , (fireBall_x , fireBall_y))

def drawBat():
	batCount = 1;
	gameDisplay.blit(bat1 , (250 , 250))

def batAttack():
	while not (x >= cac_x and x <= cac_x.get_size()[0]):
		for i in range ( 	0 , math.floor(math.sqrt( math.pow( (bat_y - y ) , 2 ) + math.pow( ( bat_x - x) , 2 ) ) )	) : 
			temp_x = bat_x
			temp_y = bat_y+(bat_y.get_size[1])
			gameDisplay.blit(batFire , ( temp_x , temp_y ) )
			temp_x += 1
			tmep_y += 1

def updateBat():
	now = pygame.time.get_ticks()

	cur = bat1;
	if now - last_update >= update_delay:
		if batCount%3 + 1 == 1:                                                                                 
			gameDisplay.blit(bat1 , (bat_x , bat_y))
			global batCount
			batCount += 1 
			global last_update 
			last_update = now
			global curBat
			curBat = bat1
			# print 'BAT UPDATED'
		elif batCount%3 + 1 == 2:
			gameDisplay.blit(bat2 , (bat_x , bat_y))
			global batCount
			batCount+=1
			global last_update 
			last_update = now
			global curBat
			curBat = bat2
			# print 'BAT UPDATED'
		elif batCount%3 +1 == 3 :
			gameDisplay.blit(bat3 , (bat_x , bat_y))
			global batCount
			batCount+=1
			global last_update 
			last_update = now
			global curBat
			curBat = bat3
			# print 'BAT UPDATED'
	else:
		if(batCount%3 + 1 == 1):
			gameDisplay.blit(bat1 , (bat_x , bat_y))
		elif batCount%3 + 1 == 2:
			gameDisplay.blit(bat2 , (bat_x , bat_y))
		elif batCount%3 + 1 == 3:
			gameDisplay.blit(bat3 , (bat_x , bat_y))

def drawGround():
	for i in range (1 ,800) :
		gameDisplay.blit(groundImage , (i, 580))
		i+=50
	for i in range (1 ,800) :
		gameDisplay.blit(groundImage , (i, 575))
		i+=50
	for i in range (1 ,800) :
		gameDisplay.blit(groundImage , (i, 570))
		i+=50
	for i in range (1 ,800) :
		gameDisplay.blit(groundImage , (i, 565))
		i+=50

drawBat()

x_width = manImg.get_size()[0]
y_width = manImg.get_size()[1]

while not crashed and man_health:

	socre_display(str(score))

	gameDisplay.fill(bgColor)
	man(x,y , manImg) 
	drawGround()       
	drawFire()
	updateBat()
	drawCactus()
	drawCloud(cloud1_x , cloud1_y)
	drawCloud(cloud2_x , cloud2_y)

	cloud1_x -= 1
	cloud2_x -= 1

	fireBall_x += 50

	bat_x -= 1

	pygame.display.update()
	clock.tick(60)

	if cloud1_x < -150:
		cloud1_x = 800

	if cloud2_x < -150:
		cloud2_x = 1375
	
	if fire1_x < -150:
		fire1_x = 600

	if cac_x < -150:
		cac_x = 800

	if bat_x < -150:
		bat_x = random.randrange(650,2050)

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        crashed = True

	keys = pygame.key.get_pressed()	

	if keys[pygame.K_ESCAPE]:
		crashed = True

	if keys[pygame.K_LEFT]:
		# print 'pressed LEFT'
		cloud1_x += 20
		cloud2_x += 20

		bat_x += 22.5

		cac_x += 35

		fire1_x += 35
		# gameDisplay.fill(bgColor)
		man(x,y , manImg)
		pygame.display.update()
		clock.tick(60)
		# x-=7.5
		time.sleep(.001)

	if keys[pygame.K_RIGHT] and x < 650:
		if(toggle == 0):
			manImg = pygame.image.load('runner1.jpg')
			toggle = 1
			time.sleep(.17)
			score += 1
		else:
			manImg = pygame.image.load('runner2.jpg')
			toggle = 0
			time.sleep(.17)
			score += 1

		x_width = manImg.get_size()[0]
		y_width = manImg.get_size()[1]

		if((x + x_width) >= (fire1_x) and (x + x_width) <= (fire1_x + fire1_width)):
			message_display("GAME OVER")
			crashed = True



		cloud1_x -= 20
		cloud2_x -= 20

		bat_x -= 22.5

		cac_x -= 35

		fire1_x -= 35

		pygame.display.update()
		clock.tick(60)
# ---------------------------------------------------- More actions (disabled) ---------------------------------------------
	# if keys[pygame.K_UP] and y > 100:
	# 	print 'pressed UP'
	# 	gameDisplay.fill(bgColor)
	# 	man(x , y , manImg)
	# 	pygame.display.update()
	# 	clock.tick(60)
	# 	y-=7.5
	# 	time.sleep(.001)

	# if keys[pygame.K_DOWN] and y < 500:
	# 	print 'pressed DOWN'
	# 	gameDisplay.fill(bgColor)
	# 	man(x , y , manImg)
	# 	pygame.display.update()
	# 	clock.tick(60)
	# 	y+=7.5
	# 	time.sleep(.001)

	# if keys[pygame.K_LALT]:
	# 	print 'FIRE'
	# 	# fireBullet(x , y-20)
	# 	batAttack()
# ---------------------------------------------------------------------------------------------------------------------------
	if keys[pygame.K_SPACE]:
		bonusScore = True
		drawBat()
		# print 'JUMP'
		# Jumping UP
		for i in range(5 , 80):
			if (x >= fire1_x) and (x < fire1_x + fire1_width) and bonusScore:
				score += 5
				bonusScore = False
			# x+=1
			y-=2
			manImg = pygame.image.load('run1.jpg')
			gameDisplay.fill(bgColor)
			man(x , y , manImg)
			drawGround()
			drawCloud(cloud1_x , cloud1_y)
			drawCloud(cloud2_x , cloud2_y)
			drawFire()
			drawCactus()
			updateBat()
			bat_x -= 3.5
			pygame.display.update()
			clock.tick(60)
			cloud1_x -= .5
			cloud2_x -= .5
			fire1_x -= 1.5
			cac_x -= 1.5

			if( ((x + x_width) >= (fire1_x) and (x + x_width) <= (fire1_x + fire1_width)) and ((y <= fire1_y)and( y >= fire1_y-fire1_height)) ):
				message_display("GAME OVER")
				crashed = True


			if( ( ( (x + x_width) >= (bat_x) ) and  ( (x + x_width) <= (bat_x + bat_width)) ) and ((y <= (bat_y + bat_height))) ):
				message_display("GAME OVER")
				crashed = True

			time.sleep(.01)
		updateBat()

		# coming down
		for i in range(5 , 80):
			if (x >= fire1_x) and (x < fire1_x + fire1_width) and bonusScore:
				score += 5
				bonusScore = False
			y+=2
			manImg = pygame.image.load('run1.jpg')
			gameDisplay.fill(bgColor)
			man(x , y , manImg)
			drawGround()
			drawCloud(cloud1_x , cloud1_y)
			drawCloud(cloud2_x , cloud2_y)
			drawFire()
			drawCactus()
			updateBat()
			bat_x -= 3.5
			pygame.display.update()
			clock.tick(60)
			cloud1_x -= 0.5
			cloud2_x -= 0.5
			fire1_x -= 1.5
			cac_x -= 1.5
			if( ((x + x_width) >= (fire1_x) and (x + x_width) <= (fire1_x + fire1_width)) and ((y <= fire1_y)and( y >= fire1_y-fire1_height)) ):
				message_display("GAME OVER")
				crashed = True
			time.sleep(.01)
		updateBat()

	if score > high_score:
		high_score = score
	drawCloud(cloud1_x , cloud1_y)
	drawCloud(cloud2_x , cloud2_y)
	socre_display(str(score))
	bat_x -= 1
	
pygame.quit()
quit()