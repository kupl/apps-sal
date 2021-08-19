class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, pathes):
        node = self.root
        for p in pathes:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        node.is_end = True

    def find(self):
        ans = []

        def dfs(pathes, node):
            if node.is_end:
                ans.append('/' + '/'.join(pathes))
                return
            for p in node.children:
                dfs(pathes + [p], node.children[p])
        dfs([], self.root)
        return ans


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f.split('/')[1:])
        return trie.find()
