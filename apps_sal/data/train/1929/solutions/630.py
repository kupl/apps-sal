class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = set(words)
        self.queries = ''

    def query(self, letter: str) -> bool:
        self.queries += letter
        for word in self.stream:
            if letter == word[~0]:
                if word == self.queries[-len(word):]:
                    return True
        return False
