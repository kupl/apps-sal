class Node(object):
    def __init__(self, name, parent=''):
        self.name = name
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.node = {kingName: self.root}
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.node[parentName].addChild(childName)
        self.node[childName] = Node(childName, parentName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = [self.root.name]
        seen = set(order)

        def successor(nodeName):
            node = self.node[nodeName]
            if (not node.children or all(c in seen for c in node.children)):
                if nodeName == self.root.name:
                    return
                return successor(node.parent)
            for c in node.children:
                if c not in seen:
                    seen.add(c)
                    order.append(c)
                    return c
        while (name := successor(order[-1])):
            pass
        return [o for o in order if o not in self.deaths]
