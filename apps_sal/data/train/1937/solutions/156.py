import collections


class Node:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def setDeath(self):
        self.alive = False

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children

    def isAlive(self):
        return self.alive


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.name_node = {kingName: Node(kingName)}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        parent = self.name_node[parentName]
        parent.addChild(child)
        self.name_node[childName] = child

    def death(self, name: str) -> None:
        person = self.name_node[name]
        person.setDeath()

    def getInheritanceOrder(self) -> List[str]:

        def dfs(node):
            if node:
                name = node.getName()
                if node.isAlive():
                    order.append(name)
                children = node.getChildren()
                for child in children:
                    dfs(child)
        node = self.name_node[self.kingName]
        order = []
        dfs(node)
        return order
