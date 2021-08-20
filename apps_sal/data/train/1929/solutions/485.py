class Trie:

    def __init__(self):
        self.isWord = False
        self.children = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.StreamChecker = Trie()
        self.stack = []
        for word in words:
            self.insert(word)

    def query(self, letter: str) -> bool:
        self.stack.insert(0, letter)
        node = self.StreamChecker
        for char in self.stack:
            if node.isWord == True:
                return True
            if char not in node.children:
                return False
            node = node.children[char]
        if node.isWord == True:
            return True
        else:
            return False

    def insert(self, word):
        node = self.StreamChecker
        word = word[::-1]
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.isWord = True
