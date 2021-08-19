class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        curr.is_word = '/' + '/'.join(word)

    # def (self, node):


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            trie.insert(path.split('/')[1:])

        res = []

        def bfs(node):
            if node.is_word:
                res.append(node.is_word)
                return
            for child in list(node.children.values()):
                bfs(child)
        bfs(trie.root)
        return res
