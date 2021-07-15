EOW = '*'
class StreamChecker:
    queries = []
    
    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            node = self.root
            for c in word:
                if c in node:
                    node = node[c]
                else:
                    node[c] = {}
                    node = node[c]
            if not EOW in node:
                node[EOW] = True

    def query(self, letter: str) -> bool:
        self.queries = [q[letter] for q in self.queries if letter in q]
        if letter in self.root:
            self.queries.append(self.root[letter])
        
        return any([q for q in self.queries if EOW in q])
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

