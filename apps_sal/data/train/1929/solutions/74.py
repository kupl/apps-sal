class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.char_stream = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.char_stream.append(letter)
        return self.trie.checkStream(self.char_stream[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    def __init__(self, children, isEnd=False):
        self.children = children
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TrieNode({})

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        node = self.root
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode({})
                node = node.children[c]
                
        node.isEnd = True

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
            
        return node.isEnd
    
    
    def checkStream(self, char_stream: List[str]) -> bool:
        node = self.root
        for c in char_stream:
            if c in node.children:
                node = node.children[c]
                if node.isEnd:
                    return True
            else:
                return False
            
        return False
            

    def startsWith(self, prefix: str) -> bool:
        \"\"\"
        Returns if there is any word in the trie that starts with the given prefix.
        \"\"\"
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
