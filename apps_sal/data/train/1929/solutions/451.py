class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = {}
        for word in words:
            try:
                if self.dic[word[-1]] == 1:
                    pass
                self.dic[word[-1]].append(word)
            except:
                self.dic[word[-1]] = [word]

    def query(self, letter: str) -> bool:
        self.s += letter
        ans = False
        try:
            for w in self.dic[letter]:
                if self.s.endswith(w):
                    ans = True
        except:
            pass
        return ans
