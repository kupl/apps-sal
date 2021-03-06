class StreamChecker:

    def __init__(self, words: List[str]):
        self.st = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.st += letter
        return any((self.st.endswith(w) for w in self.dic[letter]))
