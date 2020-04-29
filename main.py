#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

pygame.init()

class GGame:
	
	@classmethod
	def clear(cls):
		pygame.quit()
		sys.exit()
	
	# ------------------------	

	def __init__(self):
		self.window = None
		self.inloop = True
	
	def createWindow(self, w, h):
		self.window = pygame.display.set_mode((w, h))
		# return self.window
	
	def loop(self):
		while self.inloop:
			for event in pygame.event.get():
				if event.type == QUIT:
					GGame.clear()
	
	# ----------------------- #

# class G

if __name__ == '__main__':
	game = GGame()
	
	game.createWindow(640, 480)
	
	game.loop()
