class DLL:
     
     def __init__(self, val, key):
         self.val = val
         self.key = key
         self.next = None
         self.prev = None
 
 class AllOne:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.hash = {}
         self.head = None
         self.tail = None
 
     def inc(self, key):
         """
         Inserts a new key <Key> with value 1. Or increments an existing key by 1.
         :type key: str
         :rtype: void
         """
         self.print_dll()
         dll = self.hash.get(key, None)
         if not dll:
             dll = DLL(1, key)
             self.insert_dll(dll)
             self.hash[key] = dll
         else:
             self.incr_dll(dll)  
         
 
     def dec(self, key):
         """
         Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
         :type key: str
         :rtype: void
         """
         self.print_dll()
         dll = self.hash.get(key, None)
         if not dll:return
         self.decr_dll(dll)
         if dll.val == 0:
             del self.hash[key]
         
 
     def getMaxKey(self):
         """
         Returns one of the keys with maximal value.
         :rtype: str
         """
         if self.head:
             return self.head.key
         return ""
         
 
     def getMinKey(self):
         """
         Returns one of the keys with Minimal value.
         :rtype: str
         """
         if self.tail:
             return self.tail.key
         return ""
         
     def insert_dll(self, dll):
         if self.tail:
             self.tail.next = dll
             self.tail.next.prev = self.tail
             self.tail = dll
         else:
             self.head = dll
             self.tail = dll
         
     def incr_dll(self, dll):
         dll.val = dll.val + 1
         while dll.prev and dll.val > dll.prev.val:
             
             prev = dll.prev
             prev_prev = dll.prev.prev
             next_node = dll.next
             
             dll.next = prev
             prev.next = next_node
             dll.prev = prev_prev
             prev.prev = dll
             
             if prev_prev:
                 prev_prev.next = dll
             else:
                 self.head = dll
             
             if next_node:
                 next_node.prev = prev
             else:
                 self.tail = prev
                 
             
     def decr_dll(self, dll):
         dll.val = dll.val - 1
         if dll.val == 0 :
             if dll.prev:
                 dll.prev.next = dll.next
             else:
                 self.head = dll.next
                                 
             if dll.next:
                 dll.next.prev = dll.prev
             else:
                 self.tail = dll.prev
         
         elif dll.next and dll.val < dll.next.val:
             next_node = dll.next
             next_next = dll.next.next
             prev = dll.prev
             
             dll.next = next_next
             dll.prev = next_node
             
             next_node.next = dll
             next_node.prev = prev
             
             if next_next:
                 next_next.prev = dll
             else:
                 self.tail = dll
             if prev:
                 prev.next = next_node
             else:
                 self.head = next_node
                 
     def print_dll(self):
         temp = self.head
         # while temp:
         #     print("%s %s" % (temp.key, str(temp.val)))
         #     temp = temp.next
         # print("End")
 
 
             
             
                 
 
 
 
 # Your AllOne object will be instantiated and called as such:
 # obj = AllOne()
 # obj.inc(key)
 # obj.dec(key)
 # param_3 = obj.getMaxKey()
 # param_4 = obj.getMinKey()
