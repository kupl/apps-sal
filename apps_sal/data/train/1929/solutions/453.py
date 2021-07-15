class Trie:
    def __init__(self):
        self.trie = {}
    
    def add(self, word):
        trie = self.trie
        for c in word[::-1]:
            trie = trie.setdefault(c, {})
        trie[\"eos\"] = {}
        
    def find(self, char_list):
        trie = self.trie
        for c in char_list:
            if c not in trie.keys():
                return False
            trie = trie[c]
            if \"eos\" in trie.keys():
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.query_list = []
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

    def query(self, letter: str) -> bool:
        self.query_list.insert(0, letter)
        return self.trie.find(self.query_list)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
