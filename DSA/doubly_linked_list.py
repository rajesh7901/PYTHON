"""

Implementation of Doubly Linked List data structure

"""



class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

    
class Doubly_linked_list:
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_doubly_linked_list_straight(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def print_doubly_linked_list_reverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev

    def append(self,value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

    def pop(self):
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        elif self.head.next is None:
            temp = self.tail
            self.head = None
            self.tail = None
        else :
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp
    
    def prepend(self,value):
        new_node  = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def pop_first(self):
        if self.head is None :
            self.head = None
            self.tail = None
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if self.length//2 > index: # 4/2 =2 > 1
            print("from head")
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            print("from tail")
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        """if index < 0 or index >= self.length:
            return Node(None)
        if self.length//2 > index: # 4/2 =2 > 1
            print("from head")
            temp = self.head
            for i in range(index):
                temp = temp.next
            
        else:
            print("from tail")
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
        temp.value = value
        return temp"""

    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index)   # 0 -> 2 -> 3 (1,1)  
            if temp:
                new_node = Node(value)
                a = temp.prev #pointer 0 
                a.next  = new_node # 0 -> 1 -> 2
                new_node.next = temp
                new_node.prev = a
                temp.prev = new_node
        self.length +=1

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index+1 == self.length:
            self.pop()
        else:
            before = self.get(index-1)
            middle = before.next
            after = before.next.next
            before.next = before.next.next
            after.prev = after.prev.prev
            middle.next = None
            middle.prev = None
        self.length -=1
        return middle
            
            

"""
None <- 1 <-> 2 <-> 3 -> None
"""

dll = Doubly_linked_list(2)
dll.prepend(1)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print_doubly_linked_list_straight()
dll.remove(3)
dll.print_doubly_linked_list_straight()
print('Reverse')
dll.print_doubly_linked_list_reverse()
