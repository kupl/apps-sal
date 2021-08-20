class TrieNode:

    def __init__(self):
        self.children = {}
        self.isend_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isend_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.search = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.search.append(letter)
        curr = self.trie.root
        i = len(self.search) - 1
        while i >= 0 and curr.children:
            char = self.search[i]
            if curr.isend_word:
                return True
            if char not in curr.children:
                return False
            curr = curr.children[char]
            i -= 1
        return curr.isend_word
