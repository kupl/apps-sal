class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.people = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.people[parentName].children.append(child)
        self.people[childName] = child

    def death(self, name: str) -> None:
        self.people[name].alive = False
        
    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.helper(self.root, res)
        return res
        
    def helper(self, root, res):
        if root.alive:
            res.append(root.name)
        if not root.children:
            return
        for child in root.children:
            self.helper(child, res)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

