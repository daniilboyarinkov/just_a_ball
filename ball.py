import pygame
import sys

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

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	clock.tick(fps)

	screen.fill((255, 100, 100))
	screen.blit(ball, ballrect)
	pygame.display.update()
	pygame.display.flip()
