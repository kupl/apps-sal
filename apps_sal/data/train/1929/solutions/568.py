class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                new_node = TrieNode()
                curr.children[ch] = new_node
            curr = curr.children[ch]
        curr.is_end = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = collections.deque()
        self.trie = Trie()
        for ch in words:
            self.trie.add(reversed(ch))
        

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr = self.trie.root
        for ch in self.stream:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
                if curr.is_end:
                    return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

