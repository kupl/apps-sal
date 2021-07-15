class Node:
    def __init__(self, name):
        self.name = name
        self.kids = []
        self.dead = False
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head = Node(kingName)
        self.table = {}
        self.table[kingName] = self.head
    def birth(self, parentName: str, childName: str) -> None:
        self.table[childName] = Node(childName)
        self.table[parentName].kids.append(self.table[childName])
        
    def death(self, name: str) -> None:
        self.table[name].dead = True
    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def helper(n):
            if not n.dead:
                ans.append(n.name)
            for k in n.kids:
                helper(k)
        helper(self.head)
        return ans
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

