class ThroneInheritance:

    def __init__(self, king: str):
        self.king = king
        self.g = defaultdict(list)
        self.dead = set()

    def birth(self, parent: str, child: str) -> None:
        self.g[parent].append(child)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:

        curOrder = []

        def recurse(u):

            curOrder.append(u)

            for v in self.g[u]:
                recurse(v)

        recurse(self.king)

        return [u for u in curOrder if u not in self.dead]
