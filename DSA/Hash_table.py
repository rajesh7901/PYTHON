"""

Hash Table Implementation using List/Array data structure

"""


class Hash_table:
    def __init__(self,size = 7):
        self.hash_map = [None] * size
        self.size = size

    def __hash(self,key):
        hash_index = 0
        for i in key:
            hash_index += ord(i)
        return hash_index % self.size
    
    def set(self,key,value):
        index =  self.__hash(key)
        if self.hash_map[index] == None:
            self.hash_map[index] = []
        for item in self.hash_map[index]:
            if item[0] == key:
                item[1] = value
                return
        self.hash_map[index].append([key,value])

    def get(self,key):
        index =  self.__hash(key)
        for item in self.hash_map[index]:
            if item[0] == key:
                return item[1] 
        return None
    
    def keys(self):
        all_key = []
        for  i in range (self.size):
            if self.hash_map[i] is not None:
                for j in range(len(self.hash_map[i])):
                    all_key.append(self.hash_map[i][j][0])
                    #print(self.hash_map[i][j][0])
        return all_key
    
    def print_hashmap(self):
        print("Index => Key : value")
        for i in range(self.size):
            print(i,'    => ',self.hash_map[i])
        
h = Hash_table()
h.set('name','Rajesh')
h.set('eman','Kumar')
h.set('age',23)
h.print_hashmap()
print('name is ',h.get("name"))
print('name is ',h.get("eman"))
print('Age is ',h.get("age"))
print('Get all keys',h.keys())

