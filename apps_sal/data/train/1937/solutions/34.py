class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True
        self.parent = None

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.people = {kingName: self.king}
        
    def successor(self, x, current_order):
        stack = [x]
        while len(stack) > 0:
            t = stack.pop()
            if t.alive:
                current_order.append(t)
            for i in t.children:
                stack.append(i)

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.people.get(parentName)
        child = Person(childName)
        self.people[childName] = child
        child.parent = parent
        parent.children = [child] + parent.children

    def death(self, name: str) -> None:
        p = self.people.get(name)
        p.alive = False

    def getInheritanceOrder(self) -> List[str]:
        result = []
        self.successor(self.king, result)
        return [i.name for i in result]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

