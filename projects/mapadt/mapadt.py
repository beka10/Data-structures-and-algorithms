'''Implementation of the Map ADT as HashTable

Author: Beka Beriashvili

'''

class HashTable:
    def __init__(self, size_init: int=16):
        '''Constructor'''
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        '''__getitem__'''
        return self.get(key)

    def __setitem__(self, key: int, value):
        '''__setitem__'''
        self.put(key, value)
    
    def __len__(self):
        '''__len__'''
        return self._size - self._keys.count(None)
    
    def __contains__(self, key):
        '''__contains__'''
        if key in self._keys:
            return True
        else:
            return False 

    def __str__(self):
        '''__str__'''
        list1 = []
        for i in self._keys:
            if i != None:
                list1.append(i)
        list2 = []
        for i in self._values:
            if i != None:
                list2.append(i) 
        list3 = dict(zip(list1, list2))
        list3 = str(list3)
        return list3


    def _hash(self, key: int, size: int):
        '''Simple hash function'''
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int=1):
        '''Simple or quadratic rehash'''
        return (old_hash + step) % size

    def put(self, key, data):
        '''Add an item to the table'''
        hash_value = self._hash(key, len(self._keys))

        if self._keys[hash_value] is None:
            self._keys[hash_value] = key
            self._values[hash_value] = data
        
        else:
            if self._keys[hash_value] == key:
                self._values[hash_value] = data  # replace
            else:
                j = 0
                next_slot = hash_value
                while self._keys[next_slot] is not None and \
                        self._keys[next_slot] != key and \
                        j < self._size:
                    j = j + 1
                    next_slot = self._rehash(hash_value, len(self._keys), j*j)

                if self._keys[next_slot] is None:
                    self._keys[next_slot] = key
                    self._values[next_slot] = data
    
                elif j == self._size:
                    raise Exception("Hash Table is full")  
                else:
                    self._values[next_slot] = data  

    def get(self, key):
        '''Get an item from the table'''
        start_slot = self._hash(key, len(self._keys))
        position = start_slot
        j = 0

        while self._keys[position] is not None and j < self._size:
            if self._keys[position] == key:
                return self._values[position]
            else:
                j = j + 1
                position = self._rehash(start_slot, len(self._keys), j*j)


    def keys(self):
        '''Return all keys'''
        list1 = []
        for i in self._keys:
            if i != None:
                list1.append(i)
        print(list1)    
        return list1    

    def values(self):
        '''Return all values'''
        list2 = []
        for i in self._values:
            if i != None:
                list2.append(i)
        print(list2)    
        return list2

    def items(self):
        '''Return all items'''
        list1 = []
        for i in self._keys:
            if i != None:
                list1.append(i)
        list2 = []
        for i in self._values:
            if i != None:
                list2.append(i) 
        list3 = list(zip(list1, list2))
        
        return list3      
