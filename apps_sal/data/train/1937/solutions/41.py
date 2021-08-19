class ThroneInheritance:
    import collections

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.dead = set([])  # names of dead people
        self.children = collections.defaultdict(list)
        self.parent = {}

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = [self.king_name]
        order_set = set(order)

        def successor(x):
            ys = [y for y in self.children[x] if y not in order_set]
            if not ys:
                if x == self.king_name:
                    return None
                return successor(self.parent[x])

            y = ys[0]
            order.append(y)
            order_set.add(y)
            return y

        p = successor(self.king_name)
        while p:
            p = successor(p)

        return [name for name in order if name not in self.dead]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
