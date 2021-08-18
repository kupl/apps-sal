class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            node = self.root
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.root
        for c in self.stream[::-1]:
            if c in node:
                node = node[c]
                if '$' in node:
                    return True
            else:
                break
        return False
