class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.s_list = []
        self.word_len = 0
        for w in words:
            tmp = self.trie
            for c in w[::-1]:
                tmp = tmp.setdefault(c, {})
            tmp['#'] = True
            self.word_len = max(self.word_len, len(w))

    def query(self, letter: str) -> bool:
        self.s_list += letter,
        self.s_list = self.s_list[-self.word_len:]
        curr = self.trie
        for c in self.s_list[::-1]:
            if c in curr:
                curr = curr[c]
                if curr.get('#', False):
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

