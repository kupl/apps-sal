class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.parents = {}
        self.children = collections.defaultdict(list)
        self.dead = set()
    
    def Successor(self, x, cur_order):
        x_children = self.children.get(x, [])
        cand = None
        for c in x_children:
            if c not in cur_order:
                cand = c
                break
        if len(x_children) == 0 or cand is None:
            if x == self.king:
                return None
            else:
                return self.Successor(self.parents[x], cur_order)
        else:
            return cand
        

    def birth(self, parentName: str, childName: str) -> None:
        self.parents[childName] = parentName
        self.children[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        res = []
        suc = self.king
        cur_order = set([suc])
        while suc:
            if suc not in self.dead:
                res.append(suc)
            cur_order.add(suc)
            suc = self.Successor(suc, cur_order)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

