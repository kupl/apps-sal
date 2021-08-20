class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead_set = set()
        self.children = collections.defaultdict(list)
        self.inheritance_order = []

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead_set.add(name)

    def successor(self, x):
        if x not in self.dead_set:
            self.inheritance_order.append(x)
        for child in self.children[x]:
            self.successor(child)

    def getInheritanceOrder(self) -> List[str]:
        self.successor(self.king)
        res = self.inheritance_order[:]
        self.inheritance_order = []
        return res
