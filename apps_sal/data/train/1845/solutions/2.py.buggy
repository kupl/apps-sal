
 class Node:
     def __init__(self, cnt):
         self.count = cnt
         self.prev = None
         self.next = None
 
 
 class AllOne(object):
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.count_key_map={}
         self.key_count_map={}
         self.count_node_map={}
         
         self.head=Node(0)
         self.tail=Node(float('inf'))
         
         self.head.next=self.tail
         self.tail.prev=self.head
         
         self.count_node_map[0]=self.head
         self.count_node_map[float('inf')]=self.tail
 
     def inc(self, key):
         """
         Inserts a new key <Key> with value 1. Or increments an existing key by 1.
         :type key: str
         :rtype: void
         """
         if key not in self.key_count_map:
             self.key_count_map[key]=0
         
         
         prev_count=self.key_count_map[key]
         prev_node=self.count_node_map[prev_count]
         
         self.key_count_map[key]+=1
         
         if prev_node.next.count!=self.key_count_map[key]:
             new_node=Node(self.key_count_map[key])
             self.insert(prev_node,new_node)
             self.count_key_map[self.key_count_map[key]]=set()
             self.count_node_map[self.key_count_map[key]]=new_node
         
         self.count_key_map[self.key_count_map[key]].add(key)
         
         if prev_count!=0:
            
            self.count_key_map[prev_count].remove(key)
            if len(self.count_key_map[prev_count])==0:
                self.count_node_map.pop(prev_count)
                self.count_key_map.pop(prev_count)
                self.delete(prev_node)
                
     
         
 
     def dec(self, key):
         """
         Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
         :type key: str
         :rtype: void
         """
         if key not in self.key_count_map:
             return 
         prev_count=self.key_count_map[key]
         prev_node=self.count_node_map[prev_count]
         
         self.key_count_map[key]-=1
         
         
         if self.key_count_map[key]==0:
            self.key_count_map.pop(key)
         else:
             if prev_node.prev.count!=self.key_count_map[key]:
                 new_node=Node(self.key_count_map[key])
                 self.insert(prev_node.prev,new_node)
                 self.count_key_map[self.key_count_map[key]]=set()
                 self.count_node_map[self.key_count_map[key]]=new_node
         
             self.count_key_map[self.key_count_map[key]].add(key) 
             
             
         self.count_key_map[prev_count].remove(key)
         if len(self.count_key_map[prev_count])==0:
                self.delete(prev_node)
                self.count_node_map.pop(prev_count)
                self.count_key_map.pop(prev_count)
             
     def getMaxKey(self):
         """
         Returns one of the keys with maximal value.
         :rtype: str
         """
         if self.head.next == self.tail:
             return ""
         x = self.count_key_map[self.tail.prev.count].pop()
         self.count_key_map[self.tail.prev.count].add(x)
         return x
         
 
     def getMinKey(self):
         """
         Returns one of the keys with Minimal value.
         :rtype: str
         """
         if self.head.next == self.tail:
             return ""
         x = self.count_key_map[self.head.next.count].pop()
         self.count_key_map[self.head.next.count].add(x)
         return x
         
     #insert 'node' after prev_node O(1) 
     def insert(self, prev_node, node):
         node.next = prev_node.next
         node.prev = prev_node
         
         node.next.prev = node
         node.prev.next = node
         
     def delete(self, node):
         node.next.prev = node.prev
         node.prev.next = node.next
