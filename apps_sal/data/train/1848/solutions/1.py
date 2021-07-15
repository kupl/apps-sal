import random
 class RandomizedCollection(object):
     def __init__(self):
         self.l = []
         self.d = collections.defaultdict(set)
 
     def insert(self, val):
         b = val not in self.d
         self.d[val].add(len(self.l))
         self.l.append(val)
         return b
 
     def remove(self, val):
         if val not in self.d:
             return False
         i, newVal = self.d[val].pop(), self.l[-1]
         if len(self.d[val]) == 0:
             del self.d[val]
         self.l[i] = newVal
         if newVal in self.d:
             self.d[newVal].add(i)
             self.d[newVal].discard(len(self.l)-1)
         self.l.pop()
         return True
 
     def getRandom(self):
         return random.choice(self.l)
