class Member:
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []
    

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.dummy = Member('')
        self.root = Member(kingName)
        self.dummy.children.append(self.root)
        self.member_table = {'king': self.root}
        
    def birth(self, parentName: str, childName: str) -> None:
        parent = self.member_table[parentName]
        child = Member(childName)
        parent.children.append(child)
        self.member_table[childName] = child

    def death(self, name: str) -> None:
        self.member_table[name].dead = True

    
    def getInheritanceOrder(self) -> List[str]:
        def dfs(root, inheritance_order):
            for child in root.children:
                if not child.dead:
                    inheritance_order.append(child.name)
                dfs(child, inheritance_order)
            return
        
        
        inheritance_order = []
        dfs(self.dummy, inheritance_order)
        return inheritance_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

