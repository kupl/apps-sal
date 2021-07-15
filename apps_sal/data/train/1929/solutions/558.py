class TrieNode:
    def __init__(self):
        self.children = [0]*26
        self.we = 0
        self.c = 0

class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TrieNode()
        
    def findIndex(self, char):
        return ord(char) - ord(\"a\")
        

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        root = self.root
        for letter in word:
            index = self.findIndex(letter)
            if not root.children[index]:
                root.children[index] = TrieNode()
            root.c += 1
            root = root.children[index]
        root.we += 1
        
        

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        root = self.root
        for letter in word:
            index = self.findIndex(letter)
            if not root.children[index]:
                return False
            root = root.children[index]
        if root.we:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        \"\"\"
        Returns if there is any word in the trie that starts with the given prefix.
        \"\"\"
        root = self.root
        for letter in prefix:
            index = self.findIndex(letter)
            if not root.children[index]:
                return False
            root = root.children[index]
        return True
        
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        self.stream = \"\"
        for word in words:
            
            self.trie.insert(word[::-1])
        

    def query(self, letter: str) -> bool:
        self.stream = self.stream + letter
        l = len(self.stream)
        for i in range(l-1, -1, -1):
            a = self.stream[i:]
            # print(self.stream[i:], self.startsWith(self.stream[i:]))
            if not self.trie.startsWith(a[::-1]):
                return False
            else:
           
                if self.trie.search(a[::-1]):
                    return True
        return False
            
        
    
    
   
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
