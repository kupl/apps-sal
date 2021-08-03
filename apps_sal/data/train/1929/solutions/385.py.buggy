class Trie:
    def __init__(self):
        self.root = {\"0\": \"0\"}
    
    def add_w(self, w):
        cn = self.root
        for i in w[::-1]:
            if i not in cn:
                cn[i] = {}
            cn = cn[i]
        cn[\"*\"] = \"*\"
    
    def search(self, w):
        cn = self.root
        for i in w[::-1]:
            if \"*\" in cn:
                return True
            if i not in cn:
                return False
            cn = cn[i]
        return \"*\" in cn


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i in words:
            self.trie.add_w(i)
        self.string = \"\"
        
    def query(self, letter: str) -> bool:
        self.string += letter
        return self.trie.search(self.string)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
