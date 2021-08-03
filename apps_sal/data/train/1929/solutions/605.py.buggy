class Node:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
class Trie:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isLeaf = True
        
    def isWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isLeaf
    
    def isPrefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
            


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for word in words:
            self.trie.addWord(word[::-1])
        
            
    def query(self, letter: str) -> bool:
        self.letters.insert(0, letter)
        
        right = 0
        
        while right < len(self.letters):
            string = \"\".join(self.letters[:right+1])
            if self.trie.isPrefix(string):
                if self.trie.isWord(string):
                    return True
                right += 1
            else:
                return False
        
        return False
