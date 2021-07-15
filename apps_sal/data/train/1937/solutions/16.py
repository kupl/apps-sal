class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def add_children(self, name):
        node = Node(name)
        self.children.append(node)
        return node

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.dead = set()
        self.lookup = dict()
        self.lookup[kingName] = self.root
        

    def birth(self, parentName: str, childName: str) -> None:
        self.lookup[childName] = self.lookup[parentName].add_children(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        results = []
        
        def dfs(x):
            nonlocal results
            
            if x.name not in self.dead:
                results.append(x.name)
            for y in x.children:
                dfs(y)
            
        dfs(self.root)
        return results
    
    
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

