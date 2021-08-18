class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _add(self, path):
        node = self.root
        for string in path.split('/'):
            if not string:
                continue
            if string not in node.children:
                node.children[string] = TrieNode()
            node = node.children[string]
        node.isEnd = True
        return

    def _isSubFolder(self, path):
        node = self.root
        for string in path.split('/'):
            if not string:
                continue
            if node.isEnd:
                return True
            node = node.children[string]
        return False

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        for path in folder:
            self._add(path)
        for path in folder:
            if not self._isSubFolder(path):
                res.append(path)
        return res
