import collections


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = collections.defaultdict(list)
        self.dead = collections.defaultdict(bool)

    def birth(self, parentName: str, childName: str) -> None:

        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:

        stack = [self.king]
        ans = []
        while stack:
            node = stack.pop()
            if not self.dead[node]:
                ans.append(node)
            for child in reversed(self.children[node]):
                stack.append(child)

        return ans
