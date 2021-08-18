class Trie:
    def __init__(self):
        self.chars = {}

    def add(self, word):
        cur = self.chars
        for ch in word:
            cur.setdefault(ch, {})
            cur = cur[ch]
        cur['

    def find(self, word):

        cur = self.chars
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return '


class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.add(reversed(word))
        self.max_len = max(words, key=lambda x: len(x))
        self.buf=[]

    def query(self, letter):
        self.buf.append(letter)
        cur=self.trie.chars
        for i in range(len(self.buf) - 1, -1, -1):
            ch=self.buf[i]
            if ch not in cur:
                return False
            if '
                return True
            cur=cur[ch]
        return False
