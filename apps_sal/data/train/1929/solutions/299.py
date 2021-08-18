class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for char in reversed(word):
                if not char in node:
                    node[char] = {}
                node = node[char]
            node['!'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for char in self.stream:
            if '!' in node:
                return True
            if not char in node:
                return False
            node = node[char]
        return '!' in node
