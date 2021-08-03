class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            node = self.trie
            for char in w:
                node.setdefault(char, {})
                node = node[char]
            node.setdefault('*', {})
        self.curr = [self.trie]

    def query(self, letter: str) -> bool:
        new_curr = [self.trie]
        ret = False
        for node in self.curr:
            if letter in node:
                node = node[letter]
                new_curr.append(node)
                if '*' in node:
                    ret = True
        self.curr = new_curr
        return ret


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
