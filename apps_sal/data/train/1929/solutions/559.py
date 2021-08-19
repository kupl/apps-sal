class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.end = '#'
        self.chars = ''
        for word in words:
            word = word[::-1]
            cnode = self.root
            word += self.end
            for c in word:
                if c in cnode:
                    cnode = cnode[c]
                else:
                    cnode[c] = {}
                    cnode = cnode[c]

    def query(self, letter: str) -> bool:
        self.chars += letter
        cnode = self.root
        for c in self.chars[::-1]:
            if c in cnode:
                cnode = cnode[c]
            else:
                return False
            if '#' in cnode:
                return True
