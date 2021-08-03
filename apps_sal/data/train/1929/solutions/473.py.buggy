class trieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class trie:
    def __init__(self):
        self.root = trieNode()
    
    def insert_reverse(self, word):
        cp = self.root
        for i in range(len(word) - 1, -1, -1):
            index = ord(word[i]) - ord('a')
            if not cp.children[index]:
                cp.children[index] = trieNode()
            cp = cp.children[index]
        
        cp.isWord = True
    
    def search(self, word):
        cp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not cp.children[index]:
                return False
            if cp.children[index].isWord:
                return True
            cp = cp.children[index]
            
        return cp.isWord
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.tt = trie()
        self.str = \"\"
        self.maxlen = 0
        for w in words:
            self.tt.insert_reverse(w)
            self.maxlen = max(self.maxlen, len(w))
        
    def query(self, letter: str) -> bool:
        self.str += letter
        word = self.str[::-1]
        if self.maxlen < len(word):
            word = word[:self.maxlen]

        return self.tt.search(word)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
