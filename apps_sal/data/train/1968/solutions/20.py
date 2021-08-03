class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        node = self.root

        for ch in path:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end = '/' + '/'.join(path)

    def find(self):
        def dfs(aggregate, node):
            if node.end:
                result.append(node.end)
                return

            for ch in node.children:
                dfs(aggregate + [ch], node.children[ch])

        result = []
        dfs([], self.root)
        return result


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return []

        trie = Trie()
        for path in folder:
            splitPaths = path.split('/')[1:]
            trie.insert(splitPaths)

        returnList = trie.find()

        return returnList
