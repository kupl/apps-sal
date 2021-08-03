class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = {}

        for i in words:
            cur = self.words
            for l in i[::-1]:
                if l not in cur:
                    cur[l] = {}
                cur = cur[l]
            cur['.'] = {}

        self.his = []

    def query(self, letter: str) -> bool:
        self.his.append(letter)
        cur = self.words
        for i in self.his[::-1]:
            if cur.get(i) == None:
                return False
            cur = cur[i]
            if '.' in cur:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
