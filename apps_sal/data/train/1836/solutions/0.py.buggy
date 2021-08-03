import random
         
 class RandomizedSet:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.dict = {}
         self.list = []
         
 
     def insert(self, val):
         """
         Inserts a value to the set. Returns true if the set did not already contain the specified element.
         :type val: int
         :rtype: bool
         """
         if val in self.dict:
             return False
         self.dict[val] = len(self.list)
         self.list.append(val)
         return True
         
 
     def remove(self, val):
         """
         Removes a value from the set. Returns true if the set contained the specified element.
         :type val: int
         :rtype: bool
         """
         if val not in self.dict:
             return False
         self.list[self.dict[val]] = self.list[-1]
         self.dict[self.list[-1]] = self.dict[val]
         self.list.pop()
         self.dict.pop(val)
         return True
 
     def getRandom(self):
         """
         Get a random element from the set.
         :rtype: int
         """
         return random.choice(self.list)
 
 
 # Your RandomizedSet object will be instantiated and called as such:
 # obj = RandomizedSet()
 # param_1 = obj.insert(val)
 # param_2 = obj.remove(val)
 # param_3 = obj.getRandom()
