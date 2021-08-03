class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for w in word[::-1]:
            if w not in p.children:
                p.children[w] = TrieNode()
            p = p.children[w]
        p.isWord = True

    def search(self, word):
        p = self.root
        for w in word[::-1]:
            if w not in p.children:
                break
            p = p.children[w]
            if p.isWord:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.letters = ''

    def query(self, letter: str) -> bool:
        self.letters += letter
        return self.trie.search(self.letters)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
