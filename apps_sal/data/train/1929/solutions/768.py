from collections import defaultdict


class StreamChecker:

    def __init__(self, words):
        def tr(): return defaultdict(tr)
        self.trie = tr()
        for w in words:
            cur_trie = self.trie[w[0]]
            for i in range(1, len(w)):
                cur_trie = cur_trie[w[i]]
            cur_trie['end'] = True
        self.tail = []

    def query(self, letter):
        self.tail = [node[letter] for node in self.tail + [self.trie] if letter in node]
        for node in self.tail:
            if 'end' in node:
                return True
        return False
