class Node:
    def __init__(self):
        self.ch = {}
        self.cnt = 0

    def build(self, words):
        for w in words:
            n = self
            for c in w:
                if c not in n.ch:
                    n.ch[c] = Node()
                n = n.ch[c]
            n.cnt += 1

    def search(self, w, first):
        ans = 0
        if first:
            ans += self.cnt
        for c in w:
            if c not in self.ch:
                continue
            if c == w[0]:
                ans += self.ch[c].search(w, True)
            else:
                ans += self.ch[c].search(w, first)
        return ans


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        root = Node()
        root.build([sorted(set(x)) for x in words])
        ans = []
        for p in puzzles:
            ans.append(root.search(p, False))
        return ans
