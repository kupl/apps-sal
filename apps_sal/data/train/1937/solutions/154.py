class Member:
    def __init__(self,name):
        self.name = name
        self.children = list()
        self.isAlive = True
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = dict()
        self.king = Member(kingName)
        self.kingdom[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.kingdom[parentName]
        child  = Member(childName)
        self.kingdom[childName] = child
        parent.children.append(child)

    def death(self, name: str) -> None:
        member = self.kingdom[name]
        member.isAlive = False

    def getInheritanceOrder(self) -> List[str]:
        order = []
        stack = [self.kingdom[self.king.name],]
        while stack:
            member = stack.pop()
            if member.isAlive: order.append(member.name)
            for i in range(len(member.children)-1,-1,-1):
                stack.append(member.children[i])
                
        return order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

