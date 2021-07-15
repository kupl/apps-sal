class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.pointers = []
        for w in words:
            t = self.trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['*'] = '*'        

    def query(self, letter: str) -> bool:
        new_ptr = self.trie
        self.pointers.append(new_ptr)
        new_pointers = []
        ret_val = False
        for p in self.pointers:
            if letter in p:
                p = p[letter]
                if '*' in p:
                    ret_val = True
                new_pointers.append(p)
        self.pointers = new_pointers
        return ret_val


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

