MAX_WORD_LEN = 2000


class StreamChecker:
    def __init__(self, words: List[str]):
        self.ring_buffer = [None] * MAX_WORD_LEN
        self.index = 0
        self.words = set(words)
        self.possible_chars = set([
            char for word in self.words for char in word
        ])

    def query(self, letter: str) -> bool:
        self.add_letter(letter)
        if letter not in self.possible_chars:
            return False

        for word in self.words:
            if word[-1] != letter:
                continue
            if self.endswith(word):
                return True
        return False

    def add_letter(self, letter):
        self.ring_buffer[self.index] = letter
        self.index = (self.index + 1) % MAX_WORD_LEN

    def endswith(self, word):
        index = (self.index - len(word)) % MAX_WORD_LEN
        for i in range(len(word)):
            if self.ring_buffer[index] != word[i]:
                return False
            index = (index + 1) % MAX_WORD_LEN
        return True
