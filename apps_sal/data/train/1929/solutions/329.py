class Trie:
    def __init__(self):
        self.end_word=False
        self.letters=[None]*26 #as there are 26 alphabets
        
    def insert(self, s):
        t=self
        for c in s:
            if t.letters[ord(c)-ord('a')]==None:
                t.letters[ord(c)-ord('a')]=Trie()
            t=t.letters[ord(c)-ord('a')]
        t.end_word=True
        
    def search(self, s):
        t=self
        for c in s:
            if t.letters[ord(c)-ord('a')]==None: return False
            t=t.letters[ord(c)-ord('a')]
            if t.end_word: return True
        return False




class StreamChecker:

    def __init__(self, words: List[str]):
        self.t=Trie()
        self.stream=collections.deque()
        for w in words:
            self.t.insert(reversed(w))
        

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

