class StreamChecker:

    def __init__(self, words: List[str]):
        self.tab = collections.defaultdict(set)
        for w in words:
            self.tab[w[-1]].add(w[::-1])
            
        self.queried = ''
        

    def query(self, letter: str) -> bool:
        self.queried = letter + self.queried
        if letter not in self.tab:
            return False
        candidates = self.tab[letter]
        for can in candidates:
            if can == self.queried[:len(can)]:
                return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

