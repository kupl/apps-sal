class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.down=None

class Skiplist:
    def __init__(self):
        self.levels=[]
        prev=None
        for i in range(16):
            node=Node(-math.inf)
            self.levels.append(node)
            if prev:
                prev.down=node
            prev=node
\t\t\t
    def _iter(self,val):
        res=[]
        l=self.levels[0]
        while l:
            while l.next and l.next.val<val:
                l=l.next
            res.append(l)
            l=l.down
        return res
\t\t
    def search(self, target: int) -> bool:
        last=self._iter(target)[-1]
        return last.next and last.next.val==target
\t\t
    def add(self, num: int) -> None:
        res=self._iter(num)
        prev=None
        for i in range(len(res)-1,-1,-1):
            node=Node(num)
            node.next,node.down=res[i].next,prev
            res[i].next=prev=node
            rand=random.random()
            if rand>0.5:
                break
\t\t\t\t
    def erase(self, num: int) -> bool:
        found=False
        res=self._iter(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.val==num:
                res[i].next=res[i].next.next
                found=True
        return found
