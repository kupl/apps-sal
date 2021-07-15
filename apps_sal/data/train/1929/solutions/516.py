import collections
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = collections.defaultdict(list)
        self.characters = ''
        for word in words:
            self.words[word[-1]].append(word)

    def query(self, letter: str) -> bool:
        self.characters += letter
        for word in self.words[letter]:
            length = len(word)
            if self.characters[-length:] == word:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

