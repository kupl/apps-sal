from collections import OrderedDict


class ThroneInheritance:

    def __init__(self, kingName: str):
        # Maintain a tree
        self._kingName = kingName
        self._family = {kingName: []}
        self._dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self._family[parentName].append(childName)
        self._family[childName] = []

    def death(self, name: str) -> None:
        self._dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self._order(self._kingName, order)
        return order

    def _order(self, name, order):
        if name not in self._dead:
            order.append(name)
        for child in self._family[name]:
            self._order(child, order)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
