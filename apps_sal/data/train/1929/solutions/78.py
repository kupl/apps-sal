class StreamChecker:

    def __init__(self, words: List[str]):
        self.entries = {}
        for word in words:
            curNode = self.entries
            for i in range(len(word)):
                cur = word[i]
                if cur not in curNode:
                    curNode[cur] = {}
                curNode = curNode[cur]
            curNode[\"#\"] = True
        self.nodes = []
        

    def query(self, letter: str) -> bool:
        res = False
        self.nodes.append(self.entries)
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
