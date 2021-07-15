class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        self.history = ''
    def query(self, letter: str) -> bool:
        self.history += letter
        return self.trie.search(self.history[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class Node():
    def __init__(self):
        self.children = {}
        self.exist = 0
    
    
class Trie():
    def __init__(self):
        self.root = Node()
    
    def insert(self, w):
        curr_node = self.root
        for c in w:
            if c not in curr_node.children:
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
        curr_node.exist = 1
    
    def search(self, w):
        curr_node = self.root
        for c in w:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
            if curr_node.exist:
                return True
        return False
