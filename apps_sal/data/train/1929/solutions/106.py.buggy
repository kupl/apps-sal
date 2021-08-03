class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.letters = \"\"
        
        for word in words:
            self.insertWord(word)

            
    def insertWord(self, word):
        node = self.root
        word = word[::-1]
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True
        
        
    def query(self, letter: str) -> bool:
        self.letters += letter
        k = 0
        n = len(self.letters)
        node = self.root
        
        for i in range(n-1, -1, -1):
            ch = self.letters[i]
            k += 1
            if ch not in node.children:
                return False
            
            node = node.children[ch]
            if k>0 and node.isWord:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
