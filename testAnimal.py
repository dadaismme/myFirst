class animal(object):
	"""docstring for animal"""
	def __init__(self, color):
		self.color = color
	def eat(self,food):
		print(self.color,'动物在吃',food)

class dog(animal):
	"""docstring for ClassName"""
	def __init__(self,name,age,height,color):
		super(dog, self).__init__(color)
		self.name = name
		self.age=age
		self.color=color
		self.__height=height
	def run(self,speed):
		print(self.name,"速度是",speed)
	def __jump(self):
		print(self.name,"在跳舞")
	def jumped(self):
		self.__jump()
	def done(self):
		print('我是子类')
		super().eat('骨头')
	def eat(self):
		print('吃香喝辣')
		
# myAnimal=animal('白色')
# myAnimal.eat('骨头')
myDog=dog('小白',4,10,'白色')
myDog.run('9km/s')
print(myDog._dog__height)
myDog.jumped()
myDog.eat()
myDog.done()
		