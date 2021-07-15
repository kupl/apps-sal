class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for w in words:
            curr = self.trie
            for c in w:
                curr = curr.setdefault(c, {})
            curr['$'] = '$'
        self.ptrs = []

    def query(self, letter: str) -> bool:
        ret, new_list = False, []
        self.ptrs.append(self.trie)
        for ptr in self.ptrs:
            if letter in ptr:
                ptr = ptr[letter]
                if '$' in ptr:
                    ret = True
                new_list.append(ptr)
        self.ptrs = new_list
        return ret

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

