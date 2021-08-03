from functools import lru_cache


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.pm = {}
        self.cm = {}
        self.p = {
            kingName: True
        }
        self.king = kingName
        self.cm[kingName] = []

    def birth(self, parentName: str, childName: str) -> None:
        self.pm[childName] = parentName

        self.cm[parentName].append(childName)

        self.cm[childName] = []

        self.p[childName] = True

    def death(self, name: str) -> None:
        self.p[name] = False

    def getInheritanceOrder(self) -> List[str]:
        x = self.king
        curOrder = [x]

        marked_childs = {}
        queue_childs = {}

        for p, v in self.cm.items():
            marked_childs[p] = set()
            queue_childs[p] = v[:]

        while True:
            res = self.successor(x, marked_childs, queue_childs)
            if res == None:
                break
            curOrder.append(res)
            x = res
        ans = []
        for p in curOrder:
            if self.p[p]:
                ans += [p]
        return ans

    def successor(self, x, marked_childs, queue_childs):
        if len(self.cm[x]) == 0 or len(queue_childs[x]) == 0:
            if self.king == x:
                return None
            else:
                return self.successor(self.pm[x], marked_childs, queue_childs)
        else:
            c = queue_childs[x].pop(0)
            marked_childs[x] = c
            return c
