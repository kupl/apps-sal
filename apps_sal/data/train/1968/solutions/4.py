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
        def dfs(direc, node):
            if node.isEnd:
                answer.append('/' + '/'.join(direc))
                return
            for char in node.children:
                dfs(direc + [char], node.children[char])

        answer = []
        dfs([], self.root)
        return answer


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:

            f = f.split('/')[1:]
            print(f)
            trie.insert(f)
        return trie.find()
