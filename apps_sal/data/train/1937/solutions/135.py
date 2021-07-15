class people:
    def __init__(self, name, dead = False, child = None):
        self.name = name
        self.dead = dead
        self.child = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        king = people(kingName)
        self.hash = {kingName: king}
        self.king = king

    def birth(self, parentName: str, childName: str) -> None:
        pp = people(childName)
        self.hash[parentName].child.append(pp)
        self.hash[childName] = pp

    def death(self, name: str) -> None:
        self.hash[name].dead = True

    def getInheritanceOrder(self):
        self.res = []
        def dfs(pp):
            print((pp.name))
            if not pp.dead:
                self.res.append(pp.name)
            for v in pp.child:
                dfs(v)
            
        dfs(self.king)
        return self.res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

