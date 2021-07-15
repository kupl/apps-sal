class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.max_len = max((len(x) for x in self.words), default=0)
        self.q = ''
        self.num_end = min(1, self.max_len)
        self.ends = {}
        for i in range(1, self.num_end + 1):
            self.ends[i] = set(x[-i:] for x in self.words if len(x) >= i)
        # print(self.ends)
        

    def query(self, letter: str) -> bool:
        self.q += letter
        if len(self.q) > self.max_len:
            self.q = self.q[1:]
        for i in range(1, self.num_end + 1):
            # print(i, self.q[-i:])
            if self.q[-i:] not in self.ends[i]:
                return False
        # print('cont', i, self.q)
        for i in range(0, self.max_len):
            # print(~i, self.q[~i:])
            if self.q[~i:] in self.words:
                # print(self.q[~i:])
                return True
        return False
        

# Standard solution for string match is Trie.
class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words:
            reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)        


# more readable Trie
class StreamChecker(object):

    def __init__(self, words):
        self.trie = {}
        self.query_letters = []        
        for word in words:
            node = self.trie
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['END'] = True
            
    def query(self, letter):
        self.query_letters.append(letter)
        node = self.trie
        for c in reversed(self.query_letters):
            if c in node:
                node = node[c]
                if 'END' in node:
                    return True
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
