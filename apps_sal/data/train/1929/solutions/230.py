class Trie(defaultdict):

    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr:
                curr[ch] = Trie()
            curr = curr[ch]
        curr['*'] = True

    def searchWord(self, word) -> bool:
        curr = self
        for ch in word:
            if ch in curr:
                curr = curr[ch]
            else:
                return False
            if '*' in curr:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.maxLen = 0
        for word in words:
            self.maxLen = max(self.maxLen, len(word))
            self.trie.addWord(word[::-1])
        self.history = []

    def query(self, letter: str) -> bool:
        if len(self.history) == self.maxLen:
            self.history.pop(0)
        self.history.append(letter)
        return self.trie.searchWord(''.join(self.history[::-1]))
