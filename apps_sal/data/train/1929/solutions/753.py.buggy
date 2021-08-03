class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if not (c in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_node = True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.str = \"\"
        for word in words:
            self.trie.insert(word[::-1])
        

    def query(self, letter: str) -> bool:
        self.str += letter
        cur = self.trie.root
        for c in self.str[::-1]:
            if(c in cur.children):
                cur = cur.children[c]
                if(cur.end_node):
                    return True
            else:
                break
        return False       
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
