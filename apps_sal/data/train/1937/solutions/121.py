class Node(object):

    def __init__(self):
        self.children = []
        self.name = ''
        self.dead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self._root = Node()
        self._root.name = kingName
        self._locator = {kingName: self._root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node()
        child.name = childName
        self._locator[childName] = child
        self._locator[parentName].children.append(child)

    def death(self, name: str) -> None:
        self._locator[name].dead = True

    def getInheritanceOrder(self) -> List[str]:
        stack = []
        order = []
        current = self._root
        while True:
            if current:
                if not current.dead:
                    order.append(current.name)
                stack.extend(current.children[::-1])
                current = None
            elif len(stack) > 0:
                (current, stack) = (stack[-1], stack[:-1])
            else:
                break
        return order
