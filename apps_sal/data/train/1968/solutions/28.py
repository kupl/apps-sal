class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def find(self):
        def dfs(path, node):
            if node.isEnd:
                ans.append('/' + '/'.join(path))
                return
            for c in node.children:
                dfs(path + [c], node.children[c])

        ans = []
        dfs([], self.root)
        return ans


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:]
            trie.insert(f)
        return trie.find()
