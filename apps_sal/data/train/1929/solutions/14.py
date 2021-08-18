class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.maxlen = len(words)
        self.cache = ''
        for w in words:
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.cache += letter
        self.result = False
        k = 1
        node = self.trie.root
        while k <= len(self.cache):
            char = self.cache[-k]
            if char in node.children:
                self.result = self.result or node.children[char].isEnd
                k += 1
                node = node.children[char]
            else:
                break

        if len(self.cache) > self.maxlen:
            self.cache = self.cache[1:]
        return self.result
