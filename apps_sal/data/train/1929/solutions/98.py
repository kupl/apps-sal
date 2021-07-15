class Trie:
    def __init__(self):
        self.chars = {}
        self.isEnd = False
        self.current = self
        self.pointers = set([self])
        
    def add(self, word):
        trie = self
        for c in word:
            if c not in trie.chars:
                trie.chars[c] = Trie()
            trie = trie.chars[c]
        trie.isEnd = True
        
    def searchNext(self, char):
        newPointers = set([self])
        isWord = False
        for pointer in self.pointers:
            if char in pointer.chars:
                newPointer = pointer.chars[char]
                if newPointer.isEnd:
                    isWord = True
                newPointers.add(newPointer)
        self.pointers = newPointers
        return isWord
            

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        

    def query(self, letter: str) -> bool:
        return self.trie.searchNext(letter)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

