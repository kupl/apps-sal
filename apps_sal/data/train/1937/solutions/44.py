class ThroneInheritance:

    def __init__(self, kingName: str):
        self.parent = defaultdict(str)
        self.children = defaultdict(list)
        self.king = kingName
        self.order = []
        self.orderset = set()
        self.dead = set()

    def birth(self, p: str, c: str) -> None:
        self.parent[c] = p
        self.children[p].append(c)
        #print(self.parent)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.order = [self.king]
        self.orderset = set([self.king])
        while self.getNext(self.order[-1]):
            temp = self.getNext(self.order[-1])
            self.order.append(temp)
            self.orderset.add(temp)
        res = []
        for ele in self.order:
            if ele not in self.dead:
                res.append(ele)
        return res
    
    def getNext(self, cur):
        if not self.children[cur] or self.check(cur):
            if cur == self.king:
                return None
            else:
                return self.getNext(self.parent[cur])
        else:
            for child in self.children[cur]:
                if child not in self.orderset:
                    return child
    
    def check(self, cur):
        for child in self.children[cur]:
            if child not in self.orderset:
                return False
        return True
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

