class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {}
        for w in words:
            dic = self.dic
            for c in w[::-1]:
                if not c in dic:
                    dic[c] = {}
                dic = dic[c]
            dic['#'] = True
        self.stack = []

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        dic = self.dic
        for c in self.stack[::-1]:
            if '#' in dic:
                return True
            if c not in dic:
                return False
            dic = dic[c]
        return dic.get('#', False)
