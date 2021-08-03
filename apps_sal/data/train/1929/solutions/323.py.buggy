from collections import deque

class TrieNode:
    def __init__(self, val):
        self.end = False
        self.children = {}
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode(-1)
    
    def add(self, word):
        root = self.root
        for ch in word:
            children = root.children
            if children.get(ch) == None:
                child = TrieNode(ch)
                children[ch] = child
                root = child
            else:
                root = children[ch]

        root.end = True
    
    def search(self, word):

        root = self.root
        for idx, val in enumerate(word):
            if root.children.get(val) == None:
                return False
            else:
                root = root.children[val]
                if root.end:
                    return True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        # self.words = set(words)
        self.Trie = Trie()
        self.maxlen = -1
        for w in words:
            self.maxlen = max(self.maxlen, len(w))
            rev = w[::-1]
            self.Trie.add(rev)
        self.searchArr = deque()
        

    def query(self, letter: str) -> bool:

        self.searchArr.insert(0, letter)
        if len(self.searchArr) > self.maxlen:
            self.searchArr.pop()

        tmpWord = \"\".join(self.searchArr)    
        return self.Trie.search(tmpWord)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
