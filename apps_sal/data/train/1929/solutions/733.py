class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            t = self.trie
            for c in word+'\\0':
                if c not in t: t[c] = {}
                t = t[c]
        self.nodes = [self.trie]
            
    def query(self, letter: str) -> bool:
        newNodes = [self.trie]
        ret = False
        for node in self.nodes:
            if letter in node:
                newNodes.append(node[letter])  
                if '\\0' in node[letter]: ret = True
        self.nodes = newNodes
        return ret
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

