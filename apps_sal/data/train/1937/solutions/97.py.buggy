class ThroneInheritance:

    def __init__(self, kingName: str):
        self.G = collections.defaultdict(list)
        self.dead = set()
        self.king = kingName
        self.parent = dict()
    def birth(self, parentName: str, childName: str) -> None:
        self.G[parentName].append(childName)
        self.parent[childName] = parentName
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        toVisit = collections.defaultdict(int)
        visited = set()
        ans = []
        def dfs(node, ans):
            if node not in self.dead: 
                ans.append(node)
            for nei in self.G[node]:
                dfs(nei, ans)
        dfs(self.king, ans)
        return ans
        
        \"\"\"         
Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
\"\"\"
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
