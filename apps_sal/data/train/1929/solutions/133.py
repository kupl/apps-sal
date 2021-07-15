class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.end = True

    def match(self, word):
        # print('word = ', word)
        cur = self.root
        for w in word:
            if cur.end: return True
            idx = ord(w) - ord('a')
            if cur.children[idx]:
                cur = cur.children[idx]
            else: return cur.end
        return cur.end 
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.cache = ''
        self.size = 0
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
            self.size = max(self.size, len(word))

    def query(self, letter: str) -> bool:
        self.cache += letter
        if len(self.cache) > self.size:
            self.cache = self.cache[1:]
        return self.trie.match(self.cache[::-1])
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

