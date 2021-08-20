class Node:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.d = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        self.d[childName] = Node(childName)
        self.d[parentName].addChild(self.d[childName])

    def death(self, name: str) -> None:
        self.d[name].alive = False

    def getInheritanceOrder(self) -> List[str]:

        def dfs(node):
            ans = [node.name] * node.alive
            for x in node.childs:
                ans.extend(dfs(x))
            return ans
        return dfs(self.king)
