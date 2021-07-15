class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.l = max([len(w) for w in words])
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)
                

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s[-1*self.l:].endswith(w) for w in self.dic[letter])
