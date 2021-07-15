from collections import defaultdict
 
 
 class Node(object):
     def __init__(self, val, key, prev=None, next=None):
         self.val = val
         self.keys = set()
         self.keys.add(key)
         self.prev = prev
         if prev is not None:
             prev.next = self
         self.next = next
         if next is not None:
             next.prev = self
 
 
 class AllOne(object):
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.head = None
         self.tail = None
         self.key2node = dict()
 
     def check_delete(self, node):
         if len(node.keys) == 0:
             prev = node.prev
             next = node.next
             if prev is None:  # node is self.head
                 if next is None:
                     self.head = None
                     self.tail = None
                 else:
                     self.head = next
                     self.head.prev = None
             else:
                 if next is None:  # node is self.tail
                     self.tail = prev
                     self.tail.next = None
                 else:
                     prev.next = next
                     next.prev = prev
 
     def inc(self, key):
         """
         Inserts a new key <Key> with value 1. Or increments an existing key by 1.
         :type key: str
         :rtype: void
         """
         if key not in self.key2node:
             if self.head is None:
                 new_node = Node(1, key)
                 self.head = new_node
                 self.tail = new_node
                 self.key2node[key] = new_node
             elif self.head.val == 1:
                 self.head.keys.add(key)
                 self.key2node[key] = self.head
             else:
                 new_node = Node(1, key, next=self.head)
                 self.head = new_node
                 self.head.prev = None
                 self.key2node[key] = new_node
         else:
             node = self.key2node[key]
             del self.key2node[key]
             node.keys.remove(key)
             next_node = node.next
             if next_node is None:  # node is self.tail
                 next_node = Node(node.val + 1, key, prev=node)
                 self.tail = next_node
                 self.tail.next = None
             elif next_node.val == node.val + 1:
                 next_node.keys.add(key)
             else:
                 next_node = Node(node.val + 1, key, prev=node, next=next_node)
 
             self.check_delete(node)
             self.key2node[key] = next_node
 
     def dec(self, key):
         """
         Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
         :type key: str
         :rtype: void
         """
         if key not in self.key2node:
             return
 
         node = self.key2node[key]
         del self.key2node[key]
         node.keys.remove(key)
         prev_node = node.prev
         if prev_node is None:  # node is self.head
             if node.val != 1:
                 new_node = Node(node.val - 1, key, next=node)
                 self.head = new_node
                 self.head.prev = None
                 self.key2node[key] = new_node
         elif prev_node.val == node.val - 1:
             prev_node.keys.add(key)
             self.key2node[key] = prev_node
         else:
             new_node = Node(node.val - 1, key, prev=prev_node, next=node)
             self.key2node[key] = new_node
 
         self.check_delete(node)
 
     def getMaxKey(self):
         """
         Returns one of the keys with maximal value.
         :rtype: str
         """
         return '' if self.tail is None else next(iter(self.tail.keys))
         
 
     def getMinKey(self):
         """
         Returns one of the keys with Minimal value.
         :rtype: str
         """
         return '' if self.head is None else next(iter(self.head.keys))

