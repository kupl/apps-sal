class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = sorted([ww[::-1] for ww in words])
        self.entries = {}
        self.create_trie(words)
        self.nodes = []

    def create_trie(self, word_list):
        for word in word_list:
            curNode = self.entries
            for i in range(len(word)):
                cur = word[i]
                if cur not in curNode:
                    curNode[cur] = {}
                curNode = curNode[cur]
            curNode[\"#\"] = True

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
