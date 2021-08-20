class Node:

    def __init__(self, name):
        self.name = name
        self.children = []
        pass

    def give_birth_to(self, node):
        self.children.append(node)
        return


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.name_directory = dict()
        self.root = Node(kingName)
        self.name_directory[kingName] = self.root
        pass

    def birth(self, parentName: str, childName: str) -> None:
        child_node = Node(childName)
        self.name_directory[childName] = child_node
        parent_node = self.name_directory[parentName]
        parent_node.give_birth_to(child_node)
        pass

    def death(self, name: str) -> None:
        del self.name_directory[name]
        pass

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def logic(node: Node, result: List[str]):
            if node == None:
                return
            if node.name in self.name_directory:
                result.append(node.name)
            for child in node.children:
                logic(child, result)
                pass
            return
        logic(self.root, result)
        return result
