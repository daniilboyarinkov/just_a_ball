import pygame
import sys

c = 0

width = 750
height = 450
fps = 90
speed = [9, 9]
black = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((width, height))
ball = pygame.image.load('include/ball.png')
ballrect = ball.get_rect()

pygame.display.set_caption("Ball")
clock = pygame.time.Clock()

icon = pygame.image.load('include/ball.png')
pygame.display.set_icon(icon)

background = pygame.image.load("include/background.png")
rect = background.get_rect()

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		c += 1
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		c += 1
	clock.tick(fps)

	if c >= 5 and c < 10:
		screen.fill((255, 100, 100))
		screen.blit(background, (-200, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	elif c >= 10 and c < 15:
		screen.fill((255, 100, 100))
		screen.blit(background, (-400, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	elif c >= 15 and c < 20:
		screen.fill((255, 100, 100))
		screen.blit(background, (-600, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	elif c >= 20 and c < 25:
		screen.fill((255, 100, 100))
		screen.blit(background, (-800, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	elif c >= 25 and c < 30:
		screen.fill((255, 100, 100))
		screen.blit(background, (-1000, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	elif c >= 30:
		screen.fill((255, 100, 100))
		screen.blit(background, (-1160, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
	else:
		screen.fill((255, 100, 100))
		screen.blit(background, (0, -110))
		screen.blit(ball, ballrect)
		pygame.display.update()
		pygame.display.flip()
