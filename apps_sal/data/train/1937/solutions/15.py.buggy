\"\"\"
Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
\"\"\"

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.children = collections.defaultdict(list)
        self.dead = set()
        self.king = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
    
    def getInheritanceOrder(self) -> List[str]:
        res = []
        visited = set()
        self.dfs(self.king, res, visited)
        if self.king not in self.dead:
            return [self.king] + res
        return res
        
    def dfs(self, node, res, visited):
        for nxt in self.children[node]:
            if nxt not in visited:
                visited.add(node)
                if nxt not in self.dead:
                    res.append(nxt)
                self.dfs(nxt, res, visited)
            
                
        
        
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
