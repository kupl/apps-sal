class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = []
        self.trie = {}
        for word in words:
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['EOW'] = word

    def query(self, letter: str) -> bool:
        self.stream = [letter] + self.stream
        node = self.trie
        for char in self.stream:
            if 'EOW' in node:
                return True
            if char not in node:
                return False
            node = node[char]
        return 'EOW' in node
