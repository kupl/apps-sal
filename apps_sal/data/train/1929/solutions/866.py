class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            start = self.trie
            for i, l in enumerate(w):
                if l not in start:
                    start[l] = {}
                start = start[l]
            start['
        self.past = [self.trie]

    def query(self, letter: str) -> bool:
        ans = False
        new_past = [self.trie]
        for ele in self.past:
            if letter in ele:
                if '
                    ans = True
                new_past.append(ele[letter])
        self.past = new_past
        return ans
