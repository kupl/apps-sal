class StreamChecker:
    def __init__(self, words):
        self.trie = dict()
        for word in words:
            t = self.trie
            for c in reversed(word):
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t['
        self.stack = []

    def query(self, letter):
        self.stack.append(letter)
        t = self.trie
        for c in reversed(self.stack):
            if '
                return True
            if c not in t:
                return False
            t = t[c]
        return '


class StreamChecker:
    def __init__(self, words):
        self.trie = dict()
        for word in words:
            t = self.trie
            for c in reversed(word):
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t['
        self.stack = []

    def query(self, letter):
        self.stack.append(letter)
        t = self.trie
        for c in reversed(self.stack):
            if '
                return True
            elif c in t:
                t = t[c]
            else:
                return False
        return '
