class StreamChecker:

    def __init__(self, words: List[str]):
        self.tries = [False, [[] for _ in range(26)]]
        for word in words:
            self.build(word[::-1])
        self.stream = ''

    def build(self, word):
        temp_level = self.tries
        for c in word:
            if len(temp_level[1][ord(c) - ord('a')]) == 0:
                temp_level[1][ord(c) - ord('a')] = [False, [[] for _ in range(26)]]
            temp_level = temp_level[1][ord(c) - ord('a')]

        temp_level[0] = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        temp_level = self.tries
        for c in self.stream[::-1]:
            if len(temp_level[1][ord(c) - ord('a')]) == 0:
                return False
            temp_level = temp_level[1][ord(c) - ord('a')]
            if temp_level[0]:
                return True
        return False
