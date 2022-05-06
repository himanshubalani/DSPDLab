class Queue:
	def __init__(self, mx):
		self.queue = []
		self.front = self.rear = 0
		self.maxsize = mx
	
	
	def isfull(self):
		return True if self.maxsize == self.rear else False

	def isempty(self):
		return True if self.front == self.rear else False

	def enqueue(self, item):
		if self.maxsize == self.rear :
			print("\nQueue Overflow!")
		else:
			self.queue.append(item)
			self.rear += 1

	def dequeue(self):
		if self.front == self.rear:
			print("Queue Underflow!")
		else:
			self.queue.pop(0)
			self.rear -= 1

	def display(self):
		if self.front == self.rear:
			print("\nQueue Undeflow!")
		for i in self.queue:
			print(" ", i, "|", end='')

	def peek(self):
		if self.front == self.rear:
			print("\nQueue Underflow!")
			print("\nFront Element is:",self.queue[self.front])            

q = Queue(6)
q.display()

q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)

q.display()

q.enqueue(80)


q.display()

q.dequeue()
q.dequeue()
print("\n\nafter two deletions")

q.display()

q.peek()
print("\nMade by Himanshu Balani")

