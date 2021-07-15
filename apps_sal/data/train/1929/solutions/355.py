class Trie:
    def __init__(self):
        self.letters = {}
        self.hasWord = False
    
    def addWord(self, word: str) -> None:
        if word == \"\":
            self.hasWord = True
            return
        if word[-1] not in self.letters:
            self.letters[word[-1]] = Trie()
        self.letters[word[-1]].addWord(word[:-1])
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = []
        self.trie = Trie()
        for w in words:
            self.trie.addWord(w)
        
    def query(self, letter: str) -> bool:
        t = self.trie
        self.history.append(letter)
        for x in reversed(self.history):
            if t.hasWord:
                return True
            if x not in t.letters:
                return False
            t = t.letters[x]
        return t.hasWord


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
