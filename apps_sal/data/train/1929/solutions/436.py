class Trie:
    def __init__(self):
        self.children = {}
        self.endSymbol = '*'

    def insert(self, word):
        children = self.children
        for char in word[::-1]:
            if char not in children:
                children[char] = {}
            children = children[char]
        children[self.endSymbol] = word


class StreamChecker:
    # O(n * m) Time | O(max(n, m)) Space
    # n: number of queries | m: length of longest word
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.array = []

    def query(self, letter: str) -> bool:
        self.array.insert(0, letter)
        nodes = self.trie.children
        for char in self.array:
            if self.trie.endSymbol in nodes:
                return True
            if char not in nodes:
                return False
            nodes = nodes[char]
        return self.trie.endSymbol in nodes

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
