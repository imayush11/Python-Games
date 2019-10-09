import pygame
import sys
import random
pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,1)
WHITE = (255,255,255)
BLACK = (0,0,0)
SPEED = 10
SIZE = 50
POS = (WIDTH/2, HEIGHT-2*SIZE)
score = 0
back_colour = (WHITE)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
enemysize = 50
enemypos = [random.randint(0,WIDTH-enemysize),0 ]
enemylist = [enemypos]
pygame.mixer.music.load("Greyhound.mp3")
pygame.mixer.music.play()
game_over = False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)
#collision
def collide(POS, enemypos):
	p_x = POS[0]
	p_y = POS[1]
 	e_x = enemypos[0]
	e_y = enemypos[1]
	if e_x >= p_x and e_x < (p_x + SIZE) or p_x >= e_x and p_x < (e_x + enemysize):
		if(e_y >= p_y and e_y < (p_y + SIZE)) or (p_y >= e_y and p_y < (e_y + enemysize)):
			return True
	return False
#number of enemies
def drop_enemies(enemylist):
	delay = random.random()
	if len(enemylist) < score + 2 and delay < 0.2:
		x_pos = random.randint(0, WIDTH-enemysize)
		y_pos = 0
		enemylist.append([x_pos, y_pos])	
#draw enemies
def draw_enemies(enemylist):
	for enemypos in enemylist:
		pygame.draw.rect(screen, BLUE, (enemypos[0], enemypos[1], 	enemysize, enemysize))
#update enemy position
def update_position(enemylist, score):
	for idx, enemypos in enumerate(enemylist):
		if enemypos[1] >= 0 and enemypos[1] < HEIGHT:
			enemypos[1] += SPEED
		else:
			enemylist.pop(idx)
			score +=1
	return score
#check Collision
def collision_check(enemylist, POS):
	for enemypos in enemylist:
		if collide(enemypos, POS):
			#pygame.mixer.music.play()
			return True

	return False	
#Levels
def set_levels(score, SPEED):
	if score<10:
		SPEED = 3
	else:	
		SPEED = score/3+3
	return SPEED
#Game loop	
while not game_over:
	for event in pygame.event.get():
      
		if event.type == pygame.QUIT:
                	sys.exit()
		if event.type == pygame.KEYDOWN:
			x = POS[0]
		        y = POS[1]
			if event.key == pygame.K_DOWN:
				y += SIZE
			if event.key == pygame.K_UP:
				y -= SIZE
			elif event.key == pygame.K_LEFT:
				x -= SIZE 
			elif event.key == pygame.K_RIGHT:
				x += SIZE

			POS = [x, y] 
	screen.fill(back_colour)
	

	if collide(POS, enemypos):
		game_over = True
		break
	
	drop_enemies(enemylist)
	score = update_position(enemylist, score)
	if score >= 25:
		back_colour =(BLACK)
		screen.fill(back_colour)
		if score >= 50:
			back_colour =(WHITE)
			screen.fill(back_colour)
			if score >= 75:
				back_colour =(BLACK)
				screen.fill(back_colour)
				if score >= 100:
					back_colour =(WHITE)
					screen.fill(back_colour)
					if score >= 125:
						back_colour =(BLACK)
						screen.fill(back_colour)
						if score >= 150:
							back_colour =(WHITE)
							screen.fill(back_colour)
							if score >= 175:
								back_colour =(BLACK)
								screen.fill(back_colour)
	SPEED = set_levels(score, SPEED)
	text = "Score:"	+ str(score)
	label = myFont.render(text, 1, RED)
	screen.blit(label,(WIDTH-200, HEIGHT-600))
	if collision_check(enemylist, POS):
		text = "|| GAME OVER || "
		end = myFont.render(text, 1, RED)
		screen.blit(end,(WIDTH-600, HEIGHT-300))
		game_over = True
	draw_enemies(enemylist)
        pygame.draw.rect(screen,RED,(POS[0], POS[1], SIZE, SIZE))
	clock.tick(20)
	pygame.display.update()



