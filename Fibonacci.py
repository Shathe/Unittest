class Fibonacci:

	def __init__(self, n):
		self.n = n
		self.result = None

	# Get the result
	def get(self):
		if self.result == None: 
			self.result = self._compute(self.n)
		
		return self.result

	# Compute the result once
	def _compute(self, n):
		if n == 0: return 0
		elif n == 1: return 1
		else: return self._compute(n-1) + self._compute(n-2)


