class StreamChecker:

    def char_int(self, char):
        return ord(char) - ord('a')

    def add_trie(self, trie, word, idx):
        if idx == len(word):
            trie[26] = True
            return
        idx_trie = self.char_int(word[idx])
        if not trie[idx_trie]:
            trie[idx_trie] = [None] * 27
        self.add_trie(trie[idx_trie], word, idx + 1)

    def __init__(self, words: List[str]):
        self.trie = [None] * 27
        for word in words:
            self.add_trie(self.trie, word[::-1], 0)

        self.str = []

    def query(self, letter: str) -> bool:
        self.str.append(letter)
        i = len(self.str) - 1
        trie = self.trie
        while i >= 0 and trie:
            t = trie[:]
            for j in range(len(t)):
                if t[j]:
                    t[j] = chr(ord('a') + j)
            if trie[26]:
                return True
            trie = trie[self.char_int(self.str[i])]
            i -= 1
        if trie and trie[26]:
            return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
