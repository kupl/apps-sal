class Node:
    def __init__(self, name):
        self.name = name
        self.isdead = False
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        p = Node('king')
        self.root = p
        self.dic = {kingName: p}

    def birth(self, parentName: str, childName: str) -> None:
        p = Node(childName)
        self.dic[childName] = p
        parent = self.dic[parentName]
        parent.children.append(p)

    def death(self, name: str) -> None:
        p = self.dic[name]
        p.isdead = True

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(n):
            if n and not n.isdead:
                ans.append(n.name)
            for e in n.children:
                dfs(e)
        dfs(self.root)
        return ans
