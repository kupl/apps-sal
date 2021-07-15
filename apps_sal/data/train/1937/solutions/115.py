class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.is_dead = False
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.nodes = {kingName: Node(kingName)}
        
    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.nodes[parentName].children.append(child)
        self.nodes.update({childName:child})
            

    def death(self, name: str) -> None:
        self.nodes[name].is_dead = True

    def getInheritanceOrder(self) -> List[str]:
        result = []
        seq = [self.nodes[self.root]]
        while seq:
            one = seq.pop()
            if not one.is_dead:
                result.append(one.name)
            if one.children:
                seq.extend(one.children[::-1])
            
        return result

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

