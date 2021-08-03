class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.head.word = True

    def insert(self, word):
        itr = self.head
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]
        itr.word = True

    def contains(self, word):
        itr = self.head
        for c in word:
            if c in itr.children:
                itr = itr.children[c]
                if itr.word:
                    return True
            else:
                return False
        return itr.word


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.word = []

    def query(self, letter: str) -> bool:

        self.word.append(letter)
        return self.trie.contains(self.word[::-1])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
