class StreamChecker:
    class Trie:
        def __init__(self):
            self.next = {}
            self.ending = False
            
        def add(self,s):
            if s != \"\":
                if s[0] not in self.next:
                    self.next[s[0]] = StreamChecker.Trie()
                self.next[s[0]].add(s[1:])
            else:
                self.ending = True
                
        def __contains__(self,s):
            if self.ending:
                return True
            elif s == \"\":
                return False
            elif s[-1] in self.next:
                return self.next[s[-1]].__contains__(s[:len(s)-1])
            else:
                return False
            
    def __init__(self, words: List[str]):
        self.words = self.Trie()
        for w in words: self.words.add(w[::-1])
        self.q = \"\"

    def query(self, letter: str) -> bool:
        self.q += letter
        return self.q in self.words

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
