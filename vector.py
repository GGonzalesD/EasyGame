from math import pi, atan, sin , cos

class vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

		self.id = id(self)
		self.__node = None

	# --------------------------------------
	def set_node(self, obj):
		_ = obj
		while _ != None:
			if _ == self:
				raise ReferenceError("Cadena infinita de Nodos")
			_ = _.get_node()

		self.__node = obj

	def get_node(self):
		return self.__node

	def real_poss(self):
		if self.node:
			return self.poss + self.node.real_poss()
		else:
			return self.poss
		
	# --------------------------------------

	@property
	def poss(self):
		return vector(self.x, self.y)

	@poss.setter
	def poss(self, poss_):
		self.x = poss_[0]
		self.y = poss_[1]

	@property
	def g(self):
		return (0, 0) @ self
	@property
	def l(self):
		return (0, 0) % self

	@g.setter
	def g(self, g_):
		_l = self.l

		self.x = cos( g_ * pi / 180 ) * _l
		self.y = sin( g_ * pi / 180 ) * _l

	@l.setter
	def l(self, l_):
		_g = self.g

		self.x = cos( _g * pi / 180 ) * l_
		self.y = sin( _g * pi / 180 ) * l_

	# --------------------------------------

	def __repr__(self):
		return f"<{self.x}, {self.y}>"


	def __call__(self):
		return vector(x=self.x, y=self.y)

	def __getitem__(self, index):
		if index != 0 and index != 1:
			raise IndexError(f"No existe el indice '{index}' en un vector")
		else:
			return self.x if index == 0 else self.y

	def __setitem__(self, index, value):
		if index != 0 and index != 1:
			raise IndexError(f"No existe el indice '{index}' en un vector")
		else:
			if index == 0:
				self.x = value
			else:
				self.y = value

	# ---------------------------------------

	def __neg__(self):
		return vector(-self.x, -self.y)


	def __add__(self, other):
		return vector(self.x + other[0],
					self.y + other[1])

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		return vector(self.x - other[0],
			self.y - other[1])

	def __rsub__(self, other):
		return (-self) + other

	def __mul__(self, other):
		return vector(self.x * other, self.y * other)

	def __rmul__(self, other):
		return self * other

	def __truediv__(self, other):
		return vector(self.x / other, self.y / other)


	def __mod__(self, other):
		_ = (other[0]-self.x)**2 + (other[1]-self.y)**2
		return _ ** 0.5

	def __rmod__(self, other):
		return self % other

	def __matmul__(self, other, mode=True):
		
		if mode:
			_x, _y = other[0] - self.x, other[1] - self.y
		else:
			_x, _y = self.x - other[0], self.y - other[1]

		if _x != 0:
			if _x > 0:
				_ = atan( _y / _x ) * 180 / pi
			else:
				_ = 180 + atan( _y / _x ) * 180 / pi
		else:
			_ = 90 if _y > 0 else 270

		return _ % 360

	def __rmatmul__(self, other):
		return self.__matmul__(other, mode=False)


	def __pow__(self, vec):
		return vector(self.x + cos(vec[0] * pi / 180) * vec[1], self.y + sin(vec[0] * pi / 180) * vec[1])

	# -------------------------------------

	def __iter__(self):
		return iter((self.x, self.y))

	def __rshift__(self, other):
		other[0] = self.x
		other[1] = self.y

	def __lshift__(self, other):
		self.x = other[0]
		self.y = other[1]

	def __rrshift__(self, other):
		self.__lshift__(other)

	def __rlshift__(self, other):
		self.__rshift__(other)


#     * * * * * * * * * * * * * * * * * * * * * * * *     #
#     * * * * * * * * * * * * * * * * * * * * * * * *     #

if __name__ == "__main__":

	A = vector(3, 4)
	B = vector(23,5)

	C = [1, 3]


	C << A

	print(f"A: {A}")
	print(f"B: {B}")

	print(f"C: {C}")