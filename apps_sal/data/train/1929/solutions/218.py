class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.stream = collections.deque()
        for word in words:
            node = self.root
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.root
        for ch in self.stream:
            if ch in node:
                node = node[ch]
                if '
                    return True
            else:
                return False
        return '
