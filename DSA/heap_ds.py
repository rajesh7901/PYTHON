"""

Heap Implementation using List/Array data structure

"""


class Max_Heap:
    def __init__(self):
        self.heap_list = []
    
    def insert(self,value):
        self.heap_list.append(value)
        self._heapify_up()
    
    def _heapify_up(self):
        child_index = len(self.heap_list) - 1
        parent_index = (child_index - 1) //2

        while  child_index > 0 and self.heap_list[child_index] > self.heap_list[parent_index]:
            self.heap_list[parent_index],self.heap_list[child_index] = self.heap_list[child_index],self.heap_list[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) //2

    def remove_max(self):
        heap_size = len(self.heap_list)
        if heap_size==0:
            return None
        if heap_size ==1:
            return self.heap_list.pop()
        
        max_value = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self._heapify_down()
        return max_value
    
    def _heapify_down(self):
        parent_index = 0

        while True:
            left_child_idx = parent_index * 2 + 1
            right_child_idx = parent_index * 2 + 2
            heap_size = len(self.heap_list)
            max_index = parent_index

            if left_child_idx < heap_size and self.heap_list[parent_index] < self.heap_list[left_child_idx]:
                max_index = left_child_idx
            
            if right_child_idx < heap_size and self.heap_list[max_index] < self.heap_list[right_child_idx]:
                max_index = right_child_idx
            
            if max_index != parent_index:
                self.heap_list[parent_index], self.heap_list[max_index] = self.heap_list[max_index], self.heap_list[parent_index]

                parent_index = max_index
            else:
                break
    
    def get_peek(self):
        if self.heap_list:
            return self.heap_list[0]
        return None



h1 = Max_Heap()
h1.insert(1)
h1.insert(3)
h1.insert(2)
h1.insert(0)
h1.insert(5)
h1.insert(4)
h1.insert(7)
print(h1.heap_list,'\n')

h1.remove_max()
print(h1.heap_list,'\n')
h1.remove_max()
print(h1.heap_list,'\n')
print(h1.get_peek())
#[1,2,3,4,5] min
"""
to check 
       1
      /   \
   2       3
  / \
4    5

left_parent = n//2
right_parent = (n/2) -1

left_child = n * 2 + 1
right_child = n * 2 + 2
"""
import heapq
heap = [-3, -2]
heapq.heapify(heap)
print(heap)
