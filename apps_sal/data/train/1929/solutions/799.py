class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.pointers = []
        for word in words:
            if len(word) == 0:
                continue
            for i, ch in enumerate(word):
                if i == 0:
                    self.trie[ch] = self.trie.get(ch, dict())
                    cur = self.trie[ch]
                else:
                    cur[ch] = cur.get(ch, dict())
                    cur = cur[ch]
            cur['end'] = 1

    def query(self, letter: str) -> bool:
        result = False
        pointers_new = []
        if letter in self.trie:
            pointers_new.append(self.trie[letter])
            if 'end' in self.trie[letter]:
                result = True

        for pointer in self.pointers:
            if letter not in pointer:
                continue
            pointers_new.append(pointer[letter])
            if 'end' in pointer[letter]:
                result = True
        self.pointers = pointers_new

        return result


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
