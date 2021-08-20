class StreamChecker:

    def __init__(self, words: List[str]):
        self.suffixTree = {}
        for word in set(words):
            node = self.suffixTree
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = True
        self.queries = []
        return

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        node = self.suffixTree
        for ch in self.queries[::-1]:
            if '$' in node:
                return True
            if not ch in node:
                return False
            else:
                node = node[ch]
        return '$' in node
