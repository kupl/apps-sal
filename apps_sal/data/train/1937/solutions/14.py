class Child:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dead = False


def recursive(order):
    if not order.dead:
        out = [order.name]
    else:
        out = []

    for i in order.children:
        out += recursive(i)
    return out


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.order = Child(kingName)
        self.dict = {kingName: self.order}

    def birth(self, parentName: str, childName: str) -> None:
        b = Child(childName)
        self.dict[parentName].children.append(b)
        self.dict[childName] = b

    def death(self, name: str) -> None:
        self.dict[name].dead = True

    def getInheritanceOrder(self) -> List[str]:

        return recursive(self.order)
