class TreeNode:

    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.parent = None


class ThroneInheritance:

    def __init__(self, kingName: str):

        self.dic = {}
        self.root = TreeNode(kingName)
        self.dic[kingName] = self.root
        self.dead = {}

    def birth(self, parentName: str, childName: str) -> None:

        parent_node = self.dic[parentName]
        child_node = TreeNode(childName)
        child_node.parent = parent_node
        self.dic[childName] = child_node
        parent_node.children.append(child_node)

    def death(self, name: str) -> None:

        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:

        order_lst = []

        def recurse(root):
            if root.val not in self.dead:
                order_lst.append(root.val)
            for child in root.children:
                recurse(child)

        recurse(self.root)
        return order_lst
