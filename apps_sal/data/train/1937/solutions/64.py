class Node:

    def __init__(self, name, is_king, parent):
        self.name = name
        self.is_king = is_king
        self.parent = parent
        self.children = []
        self.is_dead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName, True, None)
        self.nmap = {kingName: self.root}
        self.order_set = set()

    def successor(self, x):
        if not x.children or all((c in self.order_set for c in x.children)):
            if x.is_king:
                return None
            return self.successor(x.parent)
        else:
            for c in x.children:
                if c not in self.order_set:
                    return c

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.nmap[parentName]
        child = Node(childName, False, parent)
        self.nmap[childName] = child
        parent.children.append(child)

    def death(self, name: str) -> None:
        self.nmap[name].is_dead = True

    def getInheritanceOrder(self) -> List[str]:
        res = [self.root]
        sc = self.successor(self.root)
        while sc:
            res.append(sc)
            self.order_set.add(sc)
            sc = self.successor(sc)
        self.order_set = set()
        return [n.name for n in res if not n.is_dead]
