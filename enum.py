class Enum:
	def __init__(self):
		self.v = 0
		self.defines = dict()

	def define(self,k):
		if k in self.defines:
			raise Exception(k+" is already defined!")
		self.defines[k]=self.v
		setattr(self,k,self.v)
		self.v += 1
