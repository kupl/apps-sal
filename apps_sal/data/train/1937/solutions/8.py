from collections import defaultdict


class Node:

    def __init__(self, name):
        self.name = name
        self.childs = []
        self.live = 1


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.p2cList = defaultdict(Node)
        self.p2cList[kingName] = self.root

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.p2cList[parentName].childs.append(child)
        self.p2cList[childName] = child

    def death(self, name: str) -> None:
        self.p2cList[name].live = 0

    def getInheritanceOrder(self) -> List[str]:
        res = []
        cur = self.root
        self.helper(res, cur)
        return res

    def helper(self, res, cur):
        if cur.live == 1:
            res.append(cur.name)
        if not cur.childs:
            return
        for childname in cur.childs:
            self.helper(res, childname)
