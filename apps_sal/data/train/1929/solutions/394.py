class Trie():
    def __init__(self):
        self.dic = {}
        
    def insert(self, words):
        cur = self.dic
        for word in words:
            if word not in cur:
                cur[word] = {}
            cur = cur[word]
        cur['#'] = True
    
    def search(self, words):
        cur = self.dic
        for word in words:
            if '#' in cur:
                return True
            if word not in cur:
                return False
            cur = cur[word]
        return '#' in cur

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        #self.q = deque()
        self.s = \"\"
        for word in words:
            self.trie.insert(word[::-1])    

    def query(self, letter: str) -> bool:
        #self.q.appendleft(letter)
        self.s += letter
        return self.trie.search(self.s[::-1])
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
