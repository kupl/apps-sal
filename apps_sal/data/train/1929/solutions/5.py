class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.waitlist = []
        for word in words:
            t = self.trie
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['#'] = '#'
        
        self.origin = self.trie.copy()
        self.nodes = []

    def query(self, letter):
        res = False
        self.nodes.append(self.trie)
        new_nodes = []
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if \"#\" in node:
                    res = True
                new_nodes.append(node)
        self.nodes = new_nodes     
        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
