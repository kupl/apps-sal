class Trie:
    def __init__(self):
        self.next = {}
        self.end_here = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()

        for word in words:
            cur = self.root
            for c in word[::-1]:
                if c not in cur.__next__:
                    cur.next[c] = Trie()
                cur = cur.next[c]
            cur.end_here = True
        self.k = 2000
        self.history = deque([])

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        if len(self.history) > self.k:
            self.history.popleft()

        if letter not in self.root.__next__:
            return False

        n = len(self.history)
        cur = self.root

        for i in range(n):
            c = self.history[n - 1 - i]
            if c not in cur.__next__:
                return False
            cur = cur.next[c]
            if cur.end_here:
                return True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
