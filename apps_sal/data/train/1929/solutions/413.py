class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        r = self.root
        self.maxLen = 0
        self.q = []
        for w in words:
            w = w[::-1]
            self.maxLen = max(len(w), self.maxLen)
            temp = r
            for c in w:
                if c in temp.c:
                    temp = temp.c[c]
                else:
                    temp.c[c] = Trie()
                    temp = temp.c[c]
            temp.end = True

    def query(self, l: str) -> bool:
        q = self.q
        n = self.maxLen
        r = self.root
        q.append(l)
        if len(q) > n:
            q.pop(0)

        def dfs(s, node):
            if len(s) == 0:
                return node.end
            if node.end:
                return True
            if s[0] in node.c:
                return dfs(s[1:], node.c[s[0]])
            else:
                return False
        ans = dfs(q[::-1], r)
        return ans


class Trie:
    def __init__(self):
        self.end = False
        self.c = {}
