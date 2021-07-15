class Trie:
    def __init__(self):
        self.root = {}
    
    def create_Trie(self,word):
        cur_node = self.root
        for w in word:
            if w not in cur_node:
                cur_node[w] = {}
            cur_node = cur_node[w]
        cur_node[\"$\"] = word
        
        



class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.create_Trie(word[::-1])
        self.stream = collections.deque()
        

    def query(self, letter: str) -> bool:
        
        self.stream.appendleft(letter)
        cur_node = self.trie.root
        for char in self.stream:
            if \"$\" in cur_node:
                return True
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        return \"$\" in cur_node
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
