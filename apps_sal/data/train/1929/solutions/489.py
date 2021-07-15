from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.add(word[::-1])
        self.word = ''
        self.l = max(len(word) for word in words)
    
    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True
    
    def search(self, c):
        self.word = (c + self.word)[:self.l]
        node = self.root
        for c in self.word:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.end:
                return True
        
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)

    def query(self, letter: str) -> bool:
        return self.trie.search(letter)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

