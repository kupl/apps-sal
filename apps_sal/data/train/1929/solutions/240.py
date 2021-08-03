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
            node['#'] = {}
        # print(self.root)

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.root
        # print('=>', letter)
        for ch in self.stream:
            if ch in node:
                # print(ch)
                node = node[ch]
                if '#' in node:
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
