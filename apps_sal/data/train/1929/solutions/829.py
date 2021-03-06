class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.nodes = []
        for word in words:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['end'] = True

    def query(self, letter: str) -> bool:
        self.nodes.append(self.trie)
        res = False
        new_nodes = []
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if 'end' in node:
                    res = True
                new_nodes.append(node)
        self.nodes = new_nodes
        return res
