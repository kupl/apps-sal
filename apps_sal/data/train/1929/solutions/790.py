class StreamChecker:

    def __init__(self, words: List[str]):
        self.wordlist = []
        for w in words:
            self.wordlist.append(w[::-1])
        self.wordlist.sort()
        self.history = ''

    def query2(self, letter: str) -> bool:
        self.history = letter + self.history
        k = 0
        for i in range(len(self.history)):
            w = self.history[:i + 1]
            while w > self.wordlist[k]:
                k += 1
                if k == len(self.wordlist):
                    return False
            if w == self.wordlist[k]:
                return True
        return False

    def query(self, letter: str) -> bool:
        self.history = letter + self.history
        s = 0
        f = len(self.wordlist)
        from bisect import bisect_left
        for i in range(len(self.history)):
            indx = bisect_left(self.wordlist[s:f], self.history[:i + 1]) - 1
            if indx == -1:
                if self.wordlist[s:f][0] == self.history[:i + 1]:
                    return True
            if indx + 1 < len(self.wordlist[s:f]) and self.wordlist[s:f][indx + 1] == self.history[:i + 1]:
                return True
            tmp = s + indx + 1
            f = s + bisect_left(self.wordlist[s:f], self.history[:i] + chr(ord(self.history[i]) + 1))
            s = tmp
            if s >= f:
                return False
        return False
