class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {}
        for i in words:
            cur = self.dic
            for j in i[::-1]:
                if j not in cur:
                    cur[j] = {}
                    cur = cur[j]
                else:
                    cur = cur[j]
            cur['#'] = {}
        self.res = []

    def query(self, letter: str) -> bool:
        self.res.append(letter)
        cur = self.dic
        for i in self.res[::-1]:
            if i not in cur:
                return False
            if '#' in cur[i]:
                return True
            if i in cur:
                cur = cur[i]
        return False
