class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.stream = []
        self.word_end = -1
        for word in words:
            cur_node = self.root
            for char in word[::-1]:
                cur_node.setdefault(char, {})
                cur_node = cur_node[char]
            cur_node[self.word_end] = True

    def query(self, letter: str) -> bool:
        self.stream.insert(0, letter)
        cur_node = self.root
        for char in self.stream:
            if char not in cur_node:
                return False
            else:
                cur_node = cur_node[char]
                if self.word_end in cur_node:
                    return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
