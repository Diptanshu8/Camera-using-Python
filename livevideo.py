import pygame,sys
import pygame.camera
import pygame.locals as GLOBALS
import pygame.event as EVENTS

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
window=pygame.display.set_mode((640,480))
window.blit(image,(0,0))
while True:
	for e in EVENTS.get():
		if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
			cam.stop()
			sys.exit()
			pygame.quit()
	image = cam.get_image()
	window.blit(image,(0,0))
	pygame.display.update()
