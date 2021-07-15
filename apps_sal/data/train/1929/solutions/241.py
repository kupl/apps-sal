from collections import defaultdict

class StreamChecker:

    def __init__(self, words: List[str]):
        self.wlookup = defaultdict(set)
        self.llookup = defaultdict(set)
        self._buf = \"\"
        
        for w in words:
            self.wlookup[w[-1]].add(w[::-1])
            self.llookup[w[-1]].add(len(w))
        
        

    def query(self, letter: str) -> bool:
        self._buf = \"\".join((letter, self._buf))
        
        #print(self.wlookup, self.llookup, self._buf, letter)
        
        if letter not in self.wlookup:
            return False
        
        for l in self.llookup[letter]:
            if self._buf[:l] in self.wlookup[letter]:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
