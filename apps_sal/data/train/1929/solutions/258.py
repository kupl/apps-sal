from collections import defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = defaultdict(list)
        for word in words:
            self.words[word[-1]].append(word)
        self.l = ''

    def query(self, letter: str) -> bool:
        self.l += letter
        for i in self.words[letter]:
            if self.l.endswith(i):
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
