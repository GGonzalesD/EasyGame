#!/usr/bin/python3

import pygame, sys, os
from pygame.locals import *
import vector as Vect2

pygame.init()

class GObject(Vect2.vector):
	def __init__(self, x = 0, y = 0):
		super(GObject, self).__init__(x, y)

	@property
	def position(self):
		return self.real_poss()

	def __repr__(self):
		return f"GObject[{hex(self.id)}]({self.x}, {self.y})"

class GImage(GObject):
	def __init__(self, x = 0, y = 0, src=None):
		super(GImage, self).__init__(x, y)

		self.size = 1

		if os.path.exists(src):
			self.__src = src
			self.__image = pygame.image.load(self.__src)
			self.__imagel = self.__image.copy()
		else:
			raise FileNotFoundError(f"Imagen '{self.__src}' No encontrada")



	@property
	def src(self):
		return self.__src

	def __repr__(self):
		return f"GImage[{self.__src}]({self.x}, {self.y})"


	def draw(self):
		self.__imagel = pygame.transform.scale(self.__image, (int(self.__image.get_width() * self.size), int(self.__image.get_height()* self.size)))

		_ = self.__imagel.get_rect()
		_p = self.position

		_.left = _p.x
		_.top = _p.y

		GGame.window.blit(self.__imagel, _)
	

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
		def is_print(cls, key):
			is_min = key>=ord('a') and key<=ord('z')
			is_may = key>=ord('A') and key<=ord('Z')
			is_space_line = key == ord(' ') or key == ord('\n')

			return is_min or is_may or is_space_line

		@classmethod
		def get_prints(cls):
			_ = []
			for i in cls.group:
				if cls.is_print(i) and cls.down(i):
					_.append(chr(i))

			return _

		@classmethod
		def down(cls, key):
			if key in cls.group:
				return cls.group[key] == 0
			return False

		@classmethod
		def press(cls, key):
			if key in cls.group:
				return cls.group[key] > 0
			return False

		@classmethod
		def up(cls, key):
			if key in cls.group:
				return cls.group[key] == -1
			return False

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

	A = GImage(0, 0, "image.png")
	A.size = 0.25

	def loopfun():
		A.draw()

		
		A.y += GGame.keys.press(K_DOWN)
		A.y -= GGame.keys.press(K_UP)

		A.x += GGame.keys.press(K_RIGHT)
		A.x -= GGame.keys.press(K_LEFT)

		if GGame.keys.up(K_ESCAPE):
			print("Fin Putosss")
			GGame.exit()

		for i in GGame.keys.get_prints():
			print(end=i)
	
	GGame.createWindow(640, 480)

	GGame.loopfun = loopfun
	
	GGame.loop()
