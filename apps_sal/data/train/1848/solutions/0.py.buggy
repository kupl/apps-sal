import random
 class RandomizedCollection:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.val = []
         self.idx = {}
 
     def insert(self, val):
         """
         Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
         :type val: int
         :rtype: bool
         """
         self.val.append(val)
         if val in self.idx:
             self.idx[val].append(len(self.val) - 1)
             return False
         else:
             self.idx[val] = [len(self.val) - 1]
 
     def remove(self, val):
         """
         Removes a value from the collection. Returns true if the collection contained the specified element.
         :type val: int
         :rtype: bool
         """
         if val not in self.idx:
             return False
         #print(self.val, self.idx)
         self.val[self.idx[val][-1]] = self.val[-1]
         if self.idx[self.val[-1]][-1] != self.idx[val][-1]:
             self.idx[self.val[-1]].pop()
             self.idx[self.val[-1]].append(self.idx[val][-1])
             self.idx[self.val[-1]].sort()
         self.val.pop()
         self.idx[val].pop()
         if len(self.idx[val]) == 0:
             del self.idx[val]
         return True
 
     def getRandom(self):
         """
         Get a random element from the collection.
         :rtype: int
         """
         return random.choice(self.val)
 
 
 # Your RandomizedCollection object will be instantiated and called as such:
 # obj = RandomizedCollection()
 # param_1 = obj.insert(val)
 # param_2 = obj.remove(val)
 # param_3 = obj.getRandom()
