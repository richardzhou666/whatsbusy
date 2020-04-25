class MoneyBox:
	def __init__(self, capacity) :
		self.capacity = capacity

	def can_add(self, v):
		if  v <= self.capacity:
			return True
		return False

	def add(self, v):
		if self.can_add(v) == True:
			self.capacity -= v
		print("Sorry, the money box is full!")
		print("Only {} coin is added").format(self.capacity)
		print('Remaining: {}').format(v-self.capacity)


