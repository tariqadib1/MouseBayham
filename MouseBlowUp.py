import pygame,sys,threading
#from pygame.locals import *

GREY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
ORANGE = (255,128,0)
FireSequence = (RED,ORANGE,YELLOW,GREY,BLACK)
StartSize = 0
MaxSize = 30
RingSize = int(MaxSize/len(FireSequence))
RingSequence = list(range(0,-RingSize * len(FireSequence),-RingSize))

def ShowExplosion(pos):
	boomDic = dict(zip(FireSequence,RingSequence))
	while boomDic[BLACK] < MaxSize:		
		clock = pygame.time.Clock()
		for color in FireSequence:
			if boomDic[color]>StartSize and boomDic[color]<MaxSize:
				pygame.draw.circle(screen, color, pos, boomDic[color])
			boomDic[color] += RingSize
			pygame.display.update(pygame.Rect(pos[0]-MaxSize, pos[1]-MaxSize, MaxSize*2, MaxSize*2))
			#pygame.display.update()
			clock.tick(40)

def main():
	global screen
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			#print(event.type)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()		
			if event.type == pygame.KEYDOWN:
				print(event.key)
				#ShowExplosion((event.key,event.key))
				x = threading.Thread(target=ShowExplosion, args=((event.key,event.key),))
				x.start()
			if event.type == pygame.MOUSEBUTTONUP and event.type != pygame.MOUSEMOTION:
				print(event.pos)
				#ShowExplosion(event.pos)
				x = threading.Thread(target=ShowExplosion, args=(event.pos,))
				x.start()				
				
		pygame.display.flip()
		clock.tick(60)

if __name__ == '__main__':
	main()
