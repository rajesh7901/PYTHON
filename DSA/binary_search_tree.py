"""

Binary search tree Implementation using Doubly Linked List data structure

"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if temp.value > value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
            elif temp.value < value:
                if temp.left is None:
                    temp.left  =  new_node
                    return True
                temp = temp.left

            elif temp.value == value:
                return False#do nothing value already there

    
    def lookup(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp :
            print(temp.value)
            if temp.value == value :
                print("Value found")
                break
            elif temp.value > value:
                temp = temp.right
            elif temp.value < value:
                temp = temp.left
        else:
            print("Value not found")


bst = binary_search_tree()
print(bst.root,'\n')
bst.insert(5)
print(bst.root.value)
print("Lookup for value")
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(7)
bst.insert(8)
bst.lookup(4)
