class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isWord = True
        
    def search(self, word):
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]: 
                return False
            curr = curr.children[index]
            if curr.isWord: return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.maxLength = 0
        self.q = []
        self.size = 0
        for word in words:
            revWord = word[::-1]
            length = len(revWord)
            self.maxLength = max(self.maxLength, length)
            self.trie.addWord(revWord)
        

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        self.size += 1
        if self.size > self.maxLength:
            self.q.pop(0)
            self.size -= 1
        return self.trie.search(self.q[::-1])
            
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

