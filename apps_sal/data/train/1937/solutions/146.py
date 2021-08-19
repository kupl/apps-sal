class Node:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = deque()


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.map = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        p = self.map[parentName]
        q = Node(childName)
        p.children.appendleft(q)
        self.map[childName] = q

    def death(self, name: str) -> None:
        self.map[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        ret = []
        s = [self.root]
        while s:
            p = s.pop()
            if p.alive:
                ret.append(p.name)
            s.extend(p.children)
        return ret
