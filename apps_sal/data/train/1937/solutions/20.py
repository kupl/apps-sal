class Node:
    def __init__(self, name):
        self.name = name
        self.live = True
        self.children = []
        
    def death(self):
        self.live = False
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.d = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        self.d[childName] = Node(childName)
        self.d[parentName].children.append(self.d[childName])

    def death(self, name: str) -> None:
        self.d[name].death()

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node, ans):
            if node.live:
                ans.append(node.name)
            for ch in node.children:
                dfs(ch, ans)
        ans = []
        dfs(self.root, ans)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

