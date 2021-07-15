class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] ={}
            node = node[ch]
        node[\"$\"] = True
    def search_word(self,prefix):
        node = self.root
        
        for letter in prefix:
            if letter in node:
                node = node[letter]
                if \"$\" in node:
                    return True
            else:
                return False
        return \"$\" in node

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.cur_query = collections.deque()
        

    def query(self, letter: str) -> bool:
        self.cur_query.appendleft(letter)
        return self.trie.search_word(self.cur_query)
    
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
