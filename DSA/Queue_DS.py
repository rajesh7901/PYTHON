"""

Queue Implementation using Linked List data structure

"""
class Node:
    def __init__(self,value):
        self.value =  value 
        self.next = None

class Queue:
    def __init__(self,value):
        self.first =  Node(value)
        self.last = self.first
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if not self.last :
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if not self.first :
            return None
        
        temp = self.first
        if self.first.next is None:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next 
            temp.next = None
        self.length -= 1
        return temp.value
        
q1 = Queue(1)
q1.print_queue()
print('After enqueued ')
q1.enqueue(2)
q1.enqueue(3)
q1.print_queue()

print('removed ',q1.dequeue())
print('After dequeued ')
q1.print_queue()
print('removed ',q1.dequeue())
q1.print_queue()
print('removed ',q1.dequeue())
q1.print_queue()
print('removed ',q1.dequeue())
