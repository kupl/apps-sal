class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, w):
        t = self.trie
        for c in w + '\\0':
            if c not in t:
                t[c] = {}
            t = t[c]


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.nodes = [self.trie.trie]

    def query(self, letter: str) -> bool:
        newNodes = [self.trie.trie]
        ret = False
        for node in self.nodes:
            if letter in node:
                newNodes.append(node[letter])
                if '\\0' in node[letter]:
                    ret = True
        self.nodes = newNodes
        return ret
