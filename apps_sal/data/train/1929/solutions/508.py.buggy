class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.terminating = False
        
class Trie():
    def __init__(self):
        self.root = self.get_node()
    def get_node(self):
        return TrieNode()
    def get_index(self, ch):
        return ord(ch) - ord('a')
    def insert(self, word):
        root = self.root
        len1 = len(word)
        for i in range(len1):
            index = self.get_index(word[i])
            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        root.terminating = True
    def search(self, word):
        root = self.root
        len1 = len(word)
        for i in range(len1):
            index = self.get_index(word[i])
            
            if not root: return False
            if root.terminating: return True
            root = root.children.get(index)
        return True  if root and root.terminating else False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.ch=\"\"
        for word in words: self.trie.insert(word[::-1])
        
    def query(self, letter: str) -> bool:
        self.ch +=letter
        if len(self.ch)>2000:
            self.ch = self.ch[1:]
        return self.trie.search(self.ch[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
