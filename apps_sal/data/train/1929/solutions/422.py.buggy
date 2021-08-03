class trie_node:
    def __init__(self):
        self.d = dict()
        self.end = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = trie_node()
        self.l = \"\"
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c in node.d:
                    node = node.d[c]
                else:
                    temp = trie_node()
                    node.d[c] = temp
                    node = temp
            node.end = True

    def query(self, letter: str) -> bool:
        self.l += letter
        node = self.trie
        for c in self.l[::-1]:
            if c in node.d:
                node = node.d[c]
                if node.end:
                    return True
            else:
                return False
        
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
