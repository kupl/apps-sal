class ThroneInheritance:

    def __init__(self, kingName: str):
        self.g = defaultdict(list)
        self.king_name = kingName
        self.g[kingName] = list()
        self.parent = {}
        self.d = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.g[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.d.add(name)
        return None

    def getInheritanceOrder(self) -> List[str]:
        def successor(node, order, order_set):
            if not self.g[node] or set(self.g[node]) & order_set == set(self.g[node]):
                if node == self.king_name:
                    return
                else:
                    successor(self.parent[node], order, order_set)
            else:
                for n in self.g[node]:
                    if n not in order_set:
                        order.append(n)
                        order_set.add(n)
                        return
        order = [self.king_name]
        order_set = set(order)
        added = True
        while added:
            prev_size = len(order)
            successor(order[-1], order, order_set)
            added = prev_size < len(order)
        return [o for o in order if o not in self.d]
