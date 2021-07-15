class King:
    def __init__(self, name):
        self.name = name
        self.children = dict()

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = King(kingName)
        self.inheritTree = collections.defaultdict(King)
        self.inheritTree[kingName] = self.king
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        tree = self.inheritTree
        parentNode = tree[parentName]
        childNode = King(childName)
        parentNode.children[childName] = childNode
        tree[childName] = childNode
        

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        tree = self.inheritTree
        res = []
        
        def inorder(king, res):
            if king not in self.dead:
                res.append(king)
            child = tree[king]
            for c in child.children:
                inorder(c, res)
        
        king = self.king
        inorder(king.name, res)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

