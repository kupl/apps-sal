class StreamChecker:

    from collections import defaultdict
    
    class TrieNode:
        def __init__(self):
            self.children = defaultdict()
            
    def __init__(self, words: List[str]):
        self.stream = []
        self.root = self.TrieNode()
        curr = self.root
        for word in words:
            for c in reversed(word):
                if c in curr.children.keys():
                    curr = curr.children[c]
                else:
                    curr.children[c] = self.TrieNode()
                    curr = curr.children[c]
            curr.children[\"$\"] = self.TrieNode()
            curr = self.root                

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        curr = self.root
        for l in reversed(self.stream):
            if l in curr.children.keys():
                curr = curr.children[l]
                if \"$\" in curr.children.keys():
                    return True
            else:
                return False
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
