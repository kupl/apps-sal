class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        self.consideration = []

    def query(self, letter: str) -> bool:
        self.consideration = [node.words[letter] for node in self.consideration + [self.trie] if letter in node.words]
        return any(node.is_word for node in self.consideration)


class Trie:
    def __init__(self):
        self.is_word = False
        self.prefix = ''
        self.words = {}

    def add(self, word):
        if not word:
            self.is_word = True
            return
        if word[0] in self.words:
            self.words[word[0]].add(word[1:])
        else:
            n = Trie()
            n.prefix = self.prefix + word[0]
            self.words[word[0]] = n
            self.words[word[0]].add(word[1:])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
