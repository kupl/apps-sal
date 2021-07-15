class Trie:
    def __init__(self):
        self.root = TrieNode(\"\")
        
    def insert(self, word):
        current = self.root
        for c in word:
            if current.child[ord(c) - ord('a')] == None:
                current.child[ord(c) - ord('a')] = TrieNode(c)
            current = current.child[ord(c) - ord('a')]
        current.isEnd = True
        
    def contains(self, word):
        current = self.root
        for c in word:
            if current.child[ord(c) - ord('a')] == None:
                return False
            current = current.child[ord(c) - ord('a')]
        return current.isEnd
    
    def startsWith(self, word):
        current = self.root
        for c in word:
            if current.child[ord(c) - ord('a')] == None:
                return False
            current = current.child[ord(c) - ord('a')]
        return True
              
class TrieNode:
    def __init__(self, char):
        self.val = char
        self.isEnd = False
        self.child = [None for i in range(27)]
    

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.buff = []

    def query(self, letter: str) -> bool:
        self.buff.append(letter)
        n = len(self.buff)
        s = \"\"
        for i in range(n - 1, max(n - 2000, -1), -1):
            s += self.buff[i]
            if not self.trie.startsWith(s):
                return False
            if self.trie.contains(s):
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
