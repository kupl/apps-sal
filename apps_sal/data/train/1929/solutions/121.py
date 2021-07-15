class StreamChecker:

    

    def __init__(self, words):
        self.words = []
        self.store = {}
        self.stack = ''
        self.sample = 25
        for w in words:
            if not w:
                continue
            self.insertStore(w[::-1], self.store)

    def query(self, letter):
        self.stack += letter
        return self.queryStore(self.stack, self.store)

    def insertStore(self, w, store):
        if w[:self.sample] not in store:
            store[w[:self.sample]] = {}
        if len(w) <= self.sample:
            store[w[:self.sample]]['!'] = None
        else:
            self.insertStore(w[self.sample:], store[w[:self.sample]])

    def queryStore(self, stack, store):
        if not stack:
            return False
        s = stack[:-self.sample-1:-1]
        if s in store:
            if '!' in store[s]:
                return True
            if self.queryStore(stack[:-self.sample], store[s]):
                return True
        for i in range(1, self.sample):
            if s[:i] in store:
                return True
        return False




