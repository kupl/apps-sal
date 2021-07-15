class StreamChecker(object):
    def __init__(self, words):
        self.words = set(words)
        self.added_chars = \"\"
        self.terminal_chars = set()
        for w in words:
            self.terminal_chars.add(w[-1])

    def query(self, char):
        self.added_chars += char
        if char in self.terminal_chars:
            for w in self.words:
                if self.added_chars.endswith(w):
                    return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
