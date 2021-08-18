
class Node:
    def __init__(self):
        self.children = {}
        self.isLeaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, path: List[str]) -> None:
        node = self.root
        for directory in path:
            if directory not in node.children:
                node.children[directory] = Node()
            node = node.children[directory]
        node.isLeaf = True

    def search(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if directory not in node.children:
                return False
            node = node.children[directory]
        return node.isLeaf

    def startWith(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if directory not in node.children:
                return False
            node = node.children[directory]
        return True

    def isSubfolder(self, path: List[str]) -> bool:
        node = self.root
        for directory in path:
            if node.isLeaf:
                return True
            node = node.children[directory]
        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            directories = path.split('/')
            trie.insert(directories)

        res = []
        for path in folder:
            directories = path.split('/')
            if not trie.isSubfolder(directories):
                res.append(path)
        return res
