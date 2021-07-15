class TNode(object):
    def __init__(self):
        self.d,self.f = {}, False
class StreamChecker(object):
    def __init__(self, words):
        self.root = TNode()
        self.max_ = max(map(len, words))
        for w in words:
            cur = self.root
            for j in range(len(w)-1,-1,-1):
                if w[j] not in cur.d: cur.d[w[j]] = TNode()
                cur = cur.d[w[j]]
            cur.f = True
        self.q = collections.deque([])        

    def query(self, letter):
        self.q.appendleft(letter)
        if len(self.q) > self.max_: self.q.pop()
        cur= self.root
        for l in self.q:
            if l not in cur.d: return False
            cur = cur.d[l]
            if cur.f:
                return True
        return False
