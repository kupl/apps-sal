class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.nodes = []
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['end'] = True

    def query(self, letter: str) -> bool:
        self.nodes.append(self.trie)
        temp = False
        new_nodes = []
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if 'end' in node:
                    temp = True
                new_nodes.append(node)
        self.nodes = new_nodes
        return temp
