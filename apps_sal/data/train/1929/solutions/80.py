class StreamChecker(object):
    def __init__(self, words):
        self.words = set(words)
        self.added_chars = \"\"

    def query(self, char):
        self.added_chars += char
        for w in self.words:
            if self.added_chars.endswith(w):
                return True
        else:
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
