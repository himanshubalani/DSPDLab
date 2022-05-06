from sys import maxsize

def createStack():
	stack = []
	return stack

def isEmpty(stack):
	return len(stack) == 0

def push(stack, item):
	stack.append(item)
	print(item + " pushed to stack ")
	
def pop(stack):
	if (isEmpty(stack)):
		return str(-maxsize -1)
	
	return stack.pop()

def peek(stack):
	if (isEmpty(stack)):
		return str(-maxsize -1) 
	return stack[len(stack) - 1]

def display(stack):
	return stack
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
push(stack, str(50))
push(stack, str(60))
push(stack, str(70))
print(pop(stack),"popped from stack")
print(peek(stack),"is the top element")
print(display(stack),"is the current stack")
print("Made By Himanshu Balani")