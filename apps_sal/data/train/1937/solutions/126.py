from collections import defaultdict


class node:

    def __init__(self, name):
        self.name = name
        self.isdead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        n = node(kingName)
        self.nodes = {}
        self.nodes[kingName] = n
        self.child = defaultdict(list)
        self.child[n] = []

    def dfs(self, node):
        val = [node.name] if node.isdead == False else []
        for c in self.child[node]:
            c = self.nodes[c]
            n = self.dfs(c)
            val.extend(n)
        return val

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.nodes[parentName]
        child = node(childName)
        self.nodes[childName] = child
        self.child[parent].append(childName)

    def death(self, name: str) -> None:
        n = self.nodes[name]
        n.isdead = True

    def getInheritanceOrder(self) -> List[str]:
        n = self.nodes[self.kingName]
        return self.dfs(n)
