class StreamChecker:

    def __init__(self, words: List[str]):
        root = {}
        nodes = [root]
        for w in words:
            prev = root
            for s in w:
                if s in prev:
                    node = prev[s]
                else:
                    node = {}
                    prev[s] = node
                prev = node
            prev['None'] = None
        self.array_nodes = []
        self.root = root

    def query(self, letter: str) -> bool:
        if letter in self.root:
            self.array_nodes.append(self.root)
        nodes = []
        result = False
        for node in self.array_nodes:
            if letter in node:
                nodes.append(node[letter])
                if 'None' in node[letter]:
                    result = True
        self.array_nodes = nodes
        return result
