class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kn = kingName
        self.get_child = {}
        self.get_parent = {}
        self.is_dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.get_child:
            self.get_child[parentName][0].append(childName)
        else:
            self.get_child[parentName] = ([childName], 0)
        self.get_parent[childName] = parentName

    def death(self, name: str) -> None:
        self.is_dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        cur_order = [self.kn]
        cur_order_set = set()

        def successor(x):
            child = []
            start_index = 0
            if x in self.get_child:
                (child, start_index) = self.get_child[x]
            if len(child) == 0 or all([c in cur_order_set for c in child]):
                if x == self.kn:
                    return None
                else:
                    return successor(self.get_parent[x])
            else:
                for i in range(start_index, len(child)):
                    c = child[i]
                    if c not in cur_order_set:
                        return c
            assert False
            return None
        while cur_order[-1]:
            s = successor(cur_order[-1])
            cur_order.append(s)
            cur_order_set.add(s)
        final_cur_order = []
        for co in cur_order:
            if co and co not in self.is_dead:
                final_cur_order.append(co)
        return final_cur_order
