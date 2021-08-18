class StreamChecker:

    def __init__(self, words: List[str]):

        self.trie = {}
        for word in words:
            cur = self.trie
            for l in word:
                if l not in cur:
                    cur[l] = {}
                cur = cur[l]
            cur['
        self.stream = deque()

    def query(self, letter: str) -> bool:

        temp = deque()
        self.stream.append(self.trie)
        for p in self.stream:
            if letter in p:
                temp.append(p[letter])
        self.stream = temp
        for p in self.stream:
            if '
                return True
        return False
