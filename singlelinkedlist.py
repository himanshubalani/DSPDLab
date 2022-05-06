class Node:
   def __init__(self, data):
      self.data = data
      self.nextNode = None

def getNode(data):
   newNode = Node(data)
   return newNode;

def insertPos(headNode, position, data):
   head = headNode
   if (position < 1):	
      print("Invalid position!")
   
   if position == 1:
      newNode = Node(data)
      newNode.nextNode = headNode
      head = newNode
   else:
      while (position != 0):		
         position -= 1

         if (position == 1):
            newNode = getNode(data)
            newNode.nextNode = headNode.nextNode
            headNode.nextNode = newNode
            break
         
         headNode = headNode.nextNode
         if headNode == None:
            break		
      if position != 1:
         print("position out of range")	
   return head

def printList(head):
   while (head != None):	
      print(' ' + str(head.data), end = '')
      head = head.nextNode;
   print()
   
if __name__=='__main__':
   
   head = getNode(3);
   head.nextNode = getNode(5);
   head.nextNode.nextNode = getNode(7);
   head.nextNode.nextNode.nextNode = getNode(11);
   print("Linked list before insertion: ", end='')
   printList(head);
   data = 9
   position = 3;
   head = insertPos(head, position, data);
   print("Linked list after insertion of 9 at position 3: ", end = '')
   printList(head)