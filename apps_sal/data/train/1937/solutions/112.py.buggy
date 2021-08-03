class TreeNode:

    def __init__(self, name: str):
        self.name = name
        self.is_alive = True
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.nodes = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = TreeNode(childName)
        self.nodes[parentName].children.append(child)
        self.nodes[childName] = child

    def death(self, name: str) -> None:
        self.nodes[name].is_alive = False

    def getInheritanceOrder(self):
        \"\"\"

        :return: Array of names by inheritance order
        :rtype: list[str]
        \"\"\"
        def recursive(head: TreeNode):
            if head.is_alive:
                inherit = [head.name]
            else:
                inherit = []
            for child in head.children:
                inherit = inherit + recursive(child)
            return inherit

        return recursive(self.root)

