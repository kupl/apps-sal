class ThroneInheritance:

    class Person:

        def __init__(self, name, parent=None):
            self.parent = parent
            self.name = name
            self.children = []
            self.isAlive = True

    def __init__(self, kingName: str):
        self.h = {kingName: self.Person(kingName)}
        self.cur_king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.h[childName] = self.Person(childName, parentName)
        self.h[parentName].children.append(self.h[childName])

    def death(self, name: str) -> None:
        self.h[name].isAlive = False

    def getInheritanceOrder(self) -> List[str]:
        res = []
        stack = [self.h[self.cur_king]]
        while len(stack):
            node = stack[-1]
            stack.pop()
            if node.isAlive:
                res.append(node.name)
            for i in range(len(node.children)):
                stack.append(node.children[-1 - i])
        return res
