class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            t = self.root
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['end'] = True
        self.temp = [self.root]

    def query(self, letter: str) -> bool:
        nextTemp = []
        flag = False
        for node in self.temp:
            if letter not in node:
                continue
            node = node[letter]
            nextTemp.append(node)
            if 'end' in node:
                flag = True
        nextTemp += [self.root]
        self.temp = nextTemp
        return flag
