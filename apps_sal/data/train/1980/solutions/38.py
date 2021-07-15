class Node(object): 
    def __init__(self,val): self.val,self.next, self.down = val, None, None
        
class Skiplist(object):
    def __init__(self, levels = 30):
        self.heads = [Node(-float('inf')) for _ in range(levels)]
        for c,n in zip(self.heads, self.heads[1:]): c.down = n
                    
    def search(self, target):
        cur = self.heads[0]
        while(cur):
            if cur.__next__ is None or cur.val < target <= cur.next.val:
                if cur.__next__ and target == cur.next.val: return True
                cur = cur.down
            else: cur = cur.__next__
        return False

    def add(self, num):
        stack,cur,prev = collections.deque([]),self.heads[0], None
        while(cur):
            if cur.__next__ is None or cur.val < num  <= cur.next.val:
                stack.append(cur)
                cur = cur.down
            else: cur = cur.__next__
        while(stack):
            cur = stack.pop()
            node = Node(num)
            node.next,cur.next = cur.next, node
            if prev: node.down = prev
            prev = node
            if random.randint(0,len(self.heads)-1) < len(self.heads) -1 : break
 
    def erase(self, num):
        b,cur = False,self.heads[0]
        while(cur):
            if cur.__next__ is None or cur.val < num <= cur.next.val:
                if cur.__next__ and cur.next.val == num:  b,cur.next = True,cur.next.__next__
                cur = cur.down
            else: cur = cur.__next__   
        return b
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

