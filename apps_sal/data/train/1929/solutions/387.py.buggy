class Trie:
    def __init__(self):
        self.trie = {}
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.word = \"\"
        self.reversed_list = []
        for i in words:
            self.add_word(i[::-1])
    def add_word(self,word):
        curr = self.trie 
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr[\"*\"] = True


    def query(self, letter: str) -> bool:
        self.word +=letter
        curr = self.trie
        
        for i in self.word[::-1]:
            if \"*\" in curr:
                return True
            if i not in curr:
                return False
            curr = curr[i]
        return \"*\" in curr
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
