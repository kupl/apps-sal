from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.family = defaultdict(list)
        self.parents = {}
        self.dead = set()
        self.size = 1

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
        self.parents[childName] = parentName
        self.size += 1

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = [self.king]
        pool = set(self.king)

        def sccesssor(x, curOrder):
            if self.family[x] == [] or set(self.family[x]) <= pool:
                if x == self.king:
                    return
                else:
                    sccesssor(self.parents[x], curOrder)
            else:
                for name in self.family[x]:
                    if name not in pool:
                        curOrder.append(name)
                        pool.add(name)
                        return

        for i in range(self.size - 1):
            if ans[-1] in self.dead:
                dead = ans.pop()
                sccesssor(dead, ans)
            else:
                sccesssor(ans[-1], ans)
        if ans[-1] in self.dead:
            ans.pop()
        return ans
