class Node:

    def __init__(self, name):
        self.val = name
        self.children = []
        self.alive = True

    def birth(self, child):
        self.children.append(child)

    def death(self):
        self.alive = False

    def check_alive(self):
        return self.alive


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.d = dict()
        self.d[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.d[childName] = child
        self.d[parentName].birth(child)

    def death(self, name: str) -> None:
        self.d[name].death()

    def getInheritanceOrder(self) -> List[str]:
        rtv = []
        todo = []
        todo.append(self.king)
        while todo:
            t = todo.pop()
            if t.check_alive():
                rtv.append(t.val)
            for c in t.children[::-1]:
                todo.append(c)
        return rtv
