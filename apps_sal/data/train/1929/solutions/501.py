from collections import defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        self.Queries = ''
        self.Words = defaultdict(list)
        for w in words:
            self.Words[w[-1]].append(w)

    def query(self, letter: str) -> bool:
        self.Queries += letter
        if len(self.Queries) > 2000:
            self.Queries = self.Queries[1:]
        for k in self.Words[letter]:
            i = len(k)
            if i <= len(self.Queries):
                if self.Queries[-i:] == k:
                    return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
