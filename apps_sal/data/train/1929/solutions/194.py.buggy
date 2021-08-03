class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.stream = deque([])
        for word in words:
            node = self.root
            for ch in word[::-1]:
                node.setdefault(ch, {})
                node = node[ch]
            node['#'] = {}

        
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.root
        for i in range(len(self.stream) -1, -1, -1):
            if self.stream[i] not in node:
                return False
            node = node[self.stream[i]]
            if \"#\" in node:
                return True
        return \"#\" in node
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
