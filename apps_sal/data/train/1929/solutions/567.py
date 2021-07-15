class StreamChecker:

    def __init__(self, words: List[str]):
        self.max_len = 0
        self.dequeue = collections.deque()
        self.suffix_dict = dict()

        for w in set(words):
            self.max_len = max(self.max_len, len(w))
            for i in reversed(range(len(w))):
                suffix = \"\".join(reversed(w[i:]))
                if suffix not in self.suffix_dict:
                    self.suffix_dict[suffix] = False
                if i == 0:
                    self.suffix_dict[suffix] = True

    def query(self, letter: str) -> bool:
        if len(self.dequeue) >= self.max_len:
            self.dequeue.popleft()
        self.dequeue.append(letter)

        reversed_word = ''
        for i in reversed(range(len(self.dequeue))):
            c = self.dequeue[i]
            reversed_word = reversed_word + c

            if reversed_word in self.suffix_dict:
                if self.suffix_dict[reversed_word]:
                    return True
            else:
                return False

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
