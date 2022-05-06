class setexp:

	def __init__(self):
		self.top = -1
		self.array = []
		self.postfix = []
		self.precedence = { '-': 1,'+': 2, '*': 3, '/': 4, '^': 5}
	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "Stack Underflow"

	def push(self, op):
		self.top += 1
		self.array.append(op)

	def isOperand(self, op):
		return op.isalpha()

	def preced(self, i):
		try:
			x = self.precedence[i]
			y = self.precedence[self.peek()]
			return True if x <= y else False
		except KeyError:
			return False

	def infixToPostfix(self, exp):

		for i in exp:
			if self.isOperand(i):
				self.postfix.append(i)

			elif i == '(':
				self.push(i)

			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.postfix.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()
			else:
				while(not self.isEmpty() and self.preced(i)):
						
					if i == "^" and self.array[-1] == i:
						break
					self.postfix.append(self.pop())
				self.push(i)

		while not self.isEmpty():
			self.postfix.append(self.pop())

		print("".join(self.postfix))

exp = "a+b*(c^d-e)/f+g^h-i"
print("INFIX EXPRESSION: ")
print(exp)
str = setexp()
print("POSTFIX EXPRESSION: ")
str.infixToPostfix(exp)