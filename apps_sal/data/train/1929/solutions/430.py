class StreamChecker:

    def __init__(self, words: List[str]):
        self.word = ''
        self.dic = collections.defaultdict(set)
        for i in words:
            self.dic[i[-1]].add(i)

    def query(self, letter: str) -> bool:
        self.word += letter
        return any(self.word.endswith(i) for i in self.dic[letter])
