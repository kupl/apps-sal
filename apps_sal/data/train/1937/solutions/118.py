import collections


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.mapping = collections.defaultdict(list)
        self.deads = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.mapping[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.get_order(res, self.kingName)
        return res

    def get_order(self, res, parent):

        if parent not in self.deads:
            res.append(parent)

        for child in self.mapping[parent]:
            self.get_order(res, child)
