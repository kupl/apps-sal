class TrieNode:
    def __init__(self, val: str, children: dict, isEnd=False):
        self.val = val
        self.children = children
        self.isEnd = isEnd
        
        
class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TrieNode(None, {}, False)

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        node = self.root
        for i, l in enumerate(word):
            if l in node.children:
                node = node.children[l]
            else:
                node.children[l] = TrieNode(l, {}, i == len(word) - 1)
                node = node.children[l]
                
        node.isEnd = True

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        node = self.root
        for l in word:
            if l in node.children:
                node = node.children[l]    
            else:
                return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        \"\"\"
        Returns if there is any word in the trie that starts with the given prefix.
        \"\"\"
        node = self.root
        for l in prefix:
            if l in node.children:
                node = node.children[l]
            else:
                return False
        return True
    
    def search_for_multiple(self, letters):
        node = self.root
        
        for l in letters[::-1]:
            if l in node.children:
                node = node.children[l]
            else:
                return False
            
            if node.isEnd:
                return True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.my_trie = Trie()
        
        self.letters = []
        
        for word in words:
            self.my_trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        
        return self.my_trie.search_for_multiple(self.letters)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
