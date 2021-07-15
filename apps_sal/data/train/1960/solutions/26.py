class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Linked:
    def __init__(self, m):
        self.head = Node(1)
        cur = self.head
        for n in range(2, m+1):
            cur.next = Node(n)
            cur = cur.next
    
    def print_me(self):
        cur = self.head 
        while cur:
            print(cur.val)
            cur = cur.next
        
    def move_to_front(self, val):
        if(self.head.val == val):
            return 0
        cur = self.head
        i = 0
        #print(val)
        while cur.val != val:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next
        cur.next = self.head
        self.head = cur
        return i

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        linked = Linked(m)
        #linked.print_me()
        
        result = []
        for num in queries:
            result.append(linked.move_to_front(num))
            #linked.print_me()
        return result
