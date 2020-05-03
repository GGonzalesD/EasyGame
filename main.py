#!/usr/bin/python3

import pygame, sys
from pygame.locals import *
import vector as Vect2

pygame.init()

class GObject(Vect2.vector):
	def __init__(self, x = 0, y = 0):
		super(GObject, self).__init__(x, y)

	def __repr__(self):
		return f"GObject[{hex(self.id)}]({self.x}, {self.y})"

class GGame:
	back_color = (0, 0, 0)

	window = None
	inloop = True

	loopfun = None

	time = pygame.time.Clock()
	fps = 90
	ticks = 0

	# $$ $$ $$ $$ $$ $$ $$ $$ $ #
	class keys:
		group = {}

		@classmethod
		def down(cls, key):
			if key in cls.group:
				return cls.group[key] == 0

		@classmethod
		def press(cls, key):
			if key in cls.group:
				return cls.group[key] > 0

		@classmethod
		def up(cls, key):
			if key in cls.group:
				return cls.group[key] == -1

		@classmethod
		def loop_event(cls, event):
			if event.type == KEYDOWN:
				cls.group[event.key] = 0
			if event.type == KEYUP:
				cls.group[event.key] = -1

		@classmethod
		def loop(cls):
			for key in list(cls.group.keys()):
				if cls.group[key] != -1:
					cls.group[key] += 1
				else:
					cls.group.pop(key)


	# $$ $$ $$ $$ $$ $$ $$ $$ $ #

	@classmethod
	def exit(cls):
		pygame.quit()
		sys.exit()
	
	# ------------------------	


		# self.
	
	@classmethod
	def createWindow(cls, w, h):
		cls.window = pygame.display.set_mode((w, h))
		# return self.window
	
	@classmethod
	def loop(cls):
		while cls.inloop:
			cls.window.fill(cls.back_color)

			cls.keys.loop()

			for event in pygame.event.get():
				cls.keys.loop_event(event)

				if event.type == QUIT:
					cls.exit()

			if cls.loopfun:
				cls.loopfun()

			cls.time.tick(cls.fps)
			cls.ticks += 1
			pygame.display.update()
	
	# ----------------------- #

# class G

if __name__ == '__main__':

	A = GObject(3, 0)
	B = GObject(3, 5)
	C = GObject(2, 6)
	D = GObject(3, 6)

	A.set_node(B)
	B.set_node(C)
	C.set_node(D)
	D.set_node(A)

	def loopfun():
		if GGame.keys.up(ord('q')):
			print("Fin Putosss")
			GGame.exit()
	
	GGame.createWindow(640, 480)

	GGame.loopfun = loopfun
	
	GGame.loop()
