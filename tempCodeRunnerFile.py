class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)


list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4

list.listprint()