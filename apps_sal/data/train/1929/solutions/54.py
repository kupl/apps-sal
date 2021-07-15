class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            node = self.trie
            for char in w:
                node.setdefault(char,{})
                node = node[char]
            node.setdefault('*',w)
        self.curr = deque([self.trie])

    def query(self, letter: str) -> bool:
        ret = False
        for _ in range(len(self.curr)):
            node = self.curr.popleft()
            if letter in node:
                node = node[letter]
                self.curr.append(node)
                if '*' in node:
                    ret = True
        self.curr.append(self.trie)
        return ret


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

