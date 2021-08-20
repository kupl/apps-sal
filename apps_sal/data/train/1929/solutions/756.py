class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict()
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


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.maxlen = 0
        self.cache = collections.deque()
        for w in words:
            self.trie.insert(w[::-1])
            self.maxlen = max(self.maxlen, len(w))

    def query(self, letter: str) -> bool:
        self.cache.append(letter)
        if len(self.cache) > self.maxlen:
            self.cache.popleft()
        i = len(self.cache) - 1
        node = self.trie.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.cache[i] not in node.children:
                return False
            node = node.children[self.cache[i]]
            i -= 1
        return node.isEnd
