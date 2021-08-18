class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.data = {kingName: list()}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:

        self.data[parentName].append(childName)
        self.data[childName] = list()

    def death(self, name: str) -> None:

        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:

        out, seen = [], set()

        def _helper(person) -> None:
            if person not in seen:
                if person not in self.dead:
                    out.append(person)
            for child in self.data[person]:
                _helper(child)

        _helper(self.king)
        return out
