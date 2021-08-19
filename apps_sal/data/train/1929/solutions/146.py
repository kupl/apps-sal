class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}  # thought: reverse trie?

        self.max_len = 0  # use this as a queue of most recently used stuff
        for word in words:
            pointer = self.trie
            for char in reversed(word):
                if char not in pointer:
                    pointer[char] = {}
                pointer = pointer[char]
            pointer['&'] = True  # end character
            self.max_len = max(self.max_len, len(word))

        self.queue = deque()

    def query(self, letter: str) -> bool:
        self.queue.append(letter)
        if len(self.queue) > self.max_len:
            self.queue.popleft()

        pointer = self.trie
        for char in reversed(list(self.queue)):
            if '&' in pointer:
                return True
            if char in pointer:
                pointer = pointer[char]
            else:
                return False
        if '&' in pointer:
            return True
        else:
            return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
