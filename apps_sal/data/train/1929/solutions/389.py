class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = []

        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            if self.stream[i] not in node:
                return False
            else:
                node = node[self.stream[i]]
                if '
                    return True

        return False
