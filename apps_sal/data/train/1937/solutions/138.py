class Node:
    def __init__(self, val, childs=None):
        self.val, self.childs = val, childs if childs else []


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.name2node = {kingName: self.root}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        par = self.name2node[parentName]
        node = Node(childName)
        par.childs.append(node)
        self.name2node[childName] = node

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def helper(r):
            if r.val not in self.dead:
                ans.append(r.val)
            for child in r.childs:
                helper(child)
        ans = []
        helper(self.root)
        return ans
