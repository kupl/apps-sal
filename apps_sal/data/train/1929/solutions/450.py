class TrieNode:

    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.children = dict()


class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        i = 0
        curr = self.root
        while i < len(word):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
            i += 1
        curr.isEnd = True

    def exists(self, stream):

        def solve(node, i):
            if i < 0 or stream[i] != node.val:
                return False
            elif node.val == stream[i] and node.isEnd:
                return True
            for (key, val) in node.children.items():
                if solve(val, i - 1):
                    return True
            return False
        return any([solve(child, len(stream) - 1) for child in self.root.children.values()])

    def dfs(self):

        def solve(node, lvl):
            for child in node.children.values():
                solve(child, lvl + 1)
        solve(self.root, 0)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = []
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.trie.dfs()

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.trie.exists(self.stream)


'\ncd, f, kl\n\n             _\n            / \\  \\\n            d  f  l\n            |     |k\n            c\n\nO(max len of words)\nO(2000) = O(1) lookup\n\n'
