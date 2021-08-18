class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque([])
        self.trie = {}

        for word in words:
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for char in self.stream:
            if '$' in node:
                return True
            if char not in node:
                return False
            node = node[char]

        return '$' in node
