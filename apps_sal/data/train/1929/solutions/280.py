class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        pCrawl = self.root

        length = len(key)
        for i in range(length):
            if pCrawl.children[ord(key[i])-ord('a')] is None:
                pCrawl.children[ord(key[i])-ord('a')] = TrieNode()
            
            pCrawl = pCrawl.children[ord(key[i])-ord('a')]
        
        pCrawl.eow = True
    
    def search(self, key):
        pCrawl = prev = self.root
        length = len(key)
        
        for i in range(length):
            if pCrawl.children[ord(key[i])-ord('a')] is None:
                return False
            prev = pCrawl
            pCrawl = pCrawl.children[ord(key[i])-ord('a')]
        
        return prev.children[ord(key[i])-ord('a')].eow
            

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for key in words:
            self.trie.insert(key[::-1])
        
        self.word = ''
        

    def query(self, letter: str) -> bool:
        self.word = letter + self.word
        pCrawl = self.trie.root

        for c in self.word:
            if pCrawl.children[ord(c)-ord('a')] is not None:
                if pCrawl.children[ord(c)-ord('a')].eow:
                    return True
                pCrawl = pCrawl.children[ord(c)-ord('a')]
            else:
                return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

