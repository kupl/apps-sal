class TrieNode:
    def __init__(self, ch):
        self.ch = None
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode(None)
        for word in words:
            self.insert(word[::-1])
            
        return
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                newNode = TrieNode(ch)
                cur.children[ch] = newNode
            
            cur = cur.children[ch]
            
        cur.isWord = True
        
    def search(self, word):
        cur = self.root
        for ch in word[::-1]:
            if cur.isWord:
                return True
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            
        return cur.isWord
            


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trieTree = Trie(words)
        self.curr = ''

    def query(self, letter: str) -> bool:
        self.curr += letter
        return self.trieTree.search(self.curr)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

