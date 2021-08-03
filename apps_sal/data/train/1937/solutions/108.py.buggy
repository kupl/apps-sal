class Tree:
    
    def __init__(self, name):
        \"\"\"
        name: name of the current tree
        child: list of children trees
        \"\"\"
        self.name = name
        self.child = []
        self.alive = True
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.heritance = Tree(kingName)
        self.dict = {kingName: self.heritance}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.dict[parentName]
        child = Tree(childName)
        parent.child.append(child)
        self.dict[childName] = child

    def death(self, name: str) -> None:
        self.dict[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        # would be a dfs of the whole tree
        # without the name of dead person
        order = []
        child = [self.heritance]
        while child:
            c = child.pop()
            if c.alive:
                order.append(c.name)
            for subchild in c.child[::-1]:
                child.append(subchild)
        
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
