import sys, pygame
pygame.init()

black = 0,0,0
size = width, height = 1280, 800
screen = pygame.display.set_mode(size)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame
