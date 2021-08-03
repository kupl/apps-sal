class Trie():
    def __init__(self):
        self.isWord = False
        self.children = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.StreamChecker = Trie()
        self.letters = []
        for word in words:
            self.addWord(word)

    def query(self, letter: str) -> bool:
        self.letters.insert(0, letter)
        node = self.StreamChecker
        for letter in self.letters:
            if node.isWord == True:
                return True
            if letter not in node.children:
                return False
            node = node.children[letter]

        if node.isWord == True:
            return True
        else:
            return False

    def addWord(self, word):
        node = self.StreamChecker
        word = word[::-1]
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.isWord = True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
