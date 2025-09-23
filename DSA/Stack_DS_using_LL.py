"""

STACK Implementation using Linked List data structure

"""

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height =  1
    
    def push(self,value):
        if not self.top:
            self.top = Node(value)
            self.height =  1
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.height += 1

    def pop(self):
        if  not self.top:
            return None
        else:
            temp =  self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
        return  temp.value
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            print('|')
            temp = temp.next
        print(temp)

stack1 = Stack(1)
stack1.push(2)
stack1.push(3)
stack1.print_stack()
print('Popped ' , stack1.pop(),'\n')
stack1.print_stack()
print('Popped ' , stack1.pop(),'\n')
stack1.print_stack()
print('Popped ' , stack1.pop(),'\n')
stack1.print_stack()
print('Popped ' , stack1.pop(),'\n')
stack1.print_stack()
print('Popped ' , stack1.pop(),'\n')
stack1.print_stack()
