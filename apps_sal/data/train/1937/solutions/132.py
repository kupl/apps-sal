class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingname = kingName
        self.dead = set()
        self.m = collections.defaultdict(list)
        self.m[kingName] = []

    def birth(self, parentName: str, childName: str) -> None:
        self.m[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getorderhelper(self, name, order):
        if name not in self.dead:
            order.append(name)
        for n in self.m[name]:
            self.getorderhelper(n, order)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self.getorderhelper(self.kingname, order)
        return order
