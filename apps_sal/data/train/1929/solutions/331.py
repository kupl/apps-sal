class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self, c):
        return ord('a') - ord(c)

    def insert(self, word):
        start = self.root
        n = len(word)
        for i in range(n):
            idx = self.charToIndex(word[i])
            if not start.children[idx]:
                start.children[idx] = TrieNode()
            start = start.children[idx]
        start.isEndOfWord = True

    def search(self, word):
        start = self.root
        n = len(word)
        for i in range(n):
            idx = self.charToIndex(word[i])
            if start.children[idx] == None:
                return False
            start = start.children[idx]
            if start.isEndOfWord:
                return True
        return False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.t = Trie()
        for word in words:
            self.t.insert(word[::-1])
        self.stream = collections.deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
