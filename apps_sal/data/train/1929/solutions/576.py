from functools import reduce
from collections import deque, defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.stream = ''
        (self.letters, self.end_letter) = self.prep()

    def prep(self):
        letters = set()
        end_letter = defaultdict(list)
        self.words.sort(key=lambda x: len(x))
        for (i, word) in enumerate(self.words):
            letters = letters.union(set(word))
            end_letter[word[-1]].append(i)
        return (letters, end_letter)

    def query(self, letter: str) -> bool:
        self.stream += letter
        if letter not in self.letters:
            return False
        for i in self.end_letter.get(letter, []):
            if len(self.stream) < len(self.words[i]):
                return False
            if self.stream[-len(self.words[i]):] == self.words[i]:
                return True
        return False
