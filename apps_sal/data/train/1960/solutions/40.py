class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        root = Node(0)
        cur = root
        for i in range(1, m+1):
            newNode = Node(i)
            cur.next = newNode
            cur = newNode
        
        res = []
        for i in range(len(queries)):
            targetVal = queries[i]
            cur = root
            position = 0
            while cur.next is not None:
                if cur.next.val == targetVal:
                    res.append(position)
                    
                    # add at the beginning
                    temp = cur.next
                    cur.next = temp.next
                    temp.next = root.next
                    root.next = temp
                    break
                else:
                    cur = cur.next
                    position += 1
        return res
