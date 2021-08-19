class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.cur = ''
        self.trie = {}
        for word in words:
            word = word[::-1]
            tmp = self.trie
            for w in word:
                if w not in tmp:
                    tmp[w] = dict()
                    tmp = tmp[w]
                else:
                    tmp = tmp[w]
            tmp['#'] = None

    def query(self, letter: str) -> bool:
        self.cur += letter
        point = self.trie
        for i in range(len(self.cur) - 1, -1, -1):
            t = self.cur[i]
            if '#' in point:
                return True
            if t not in point:
                return False
            point = point[t]
        if '#' in point:
            return True
        else:
            return False
