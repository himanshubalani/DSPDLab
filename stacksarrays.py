class StackUsingArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1] 
            del(self.stack[-1])
            return lastElement
        else:
            return("Stack Already Empty")

    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        return self.stack

stack = StackUsingArray()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
lt = stack.pop()
print(lt,"popped from stack")
print(stack.printStack(),"is the current stack")
print("Made By Himanshu Balani")
