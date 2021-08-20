class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        root = self.root
        for char in reversed(word):
            child = root.children.get(char, TrieNode())
            root.children[char] = child
            root = child
        root.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        root = self.trie.root
        for char in reversed(self.letters):
            if char not in root.children:
                return False
            root = root.children[char]
            if root.isWord:
                return True
        return False
