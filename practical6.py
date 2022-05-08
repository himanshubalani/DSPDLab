class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insertfirst(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def insertafter(self, prev_node, new_data):
		if prev_node is None:
			print("the given previous node cannot be NULL")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node
		new_node.prev = prev_node
		if new_node.next:
			new_node.next.prev = new_node

	def insertlast(self, new_data):
		new_node = Node(new_data)	
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
		new_node.prev = last
		return

	def printList(self, node):
		while node:
			print(" {}".format(node.data))
			last = node
			node = node.next

llist = DoublyLinkedList()
llist.insertlast(6)
llist.insertfirst(7)
llist.insertfirst(1)
llist.insertlast(4)
llist.insertafter(llist.head.next, 8)
llist.insertfirst(2)
llist.insertlast(9)
llist.insertafter(llist.head.next, 5)

print ("Created DLL is: ")
llist.printList(llist.head)

