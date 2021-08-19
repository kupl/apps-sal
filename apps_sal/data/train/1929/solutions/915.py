class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            node = self.root
            for c in word:
                node.setdefault(c, {})
                node = node[c]
            node[''] = True
        self.ptrs = []

    def query(self, letter: str) -> bool:
        ptrs = self.ptrs
        ptrs.append(self.root)
        (i, L) = (0, len(ptrs))
        found = False
        while i < L:
            if letter in ptrs[i]:
                ptrs[i] = ptrs[i][letter]
                if '' in ptrs[i]:
                    found = True
                i += 1
            else:
                ptrs[i] = ptrs[L - 1]
                ptrs.pop()
                L -= 1
        return found
