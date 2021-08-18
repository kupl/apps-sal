from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.d = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.d[parentName].append(childName)
        return

    def death(self, name: str) -> None:
        self.dead.add(name)
        return

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def p(root):
            nonlocal ans
            if root not in self.dead:
                ans.append(root)

            for i in self.d[root]:
                p(i)
        p(self.root)
        return ans
