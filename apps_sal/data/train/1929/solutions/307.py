class TrieNode:
    def __init__(self, char):
        self.char = char
        self.accept = False
        self.children = {}

class StreamNode:
    def __init__(self, char):
        self.char = char
        self.next = None

class StreamChecker:

    def __init__(self, words: List[str]):
        self.maxlen = 0
        self.trie = TrieNode(\"\")
        i = 0
        should_continue = True
        for j in range(len(words)):
            word = words[j]
            self.maxlen = max(len(word), self.maxlen)
            p = self.trie
            for i in range(len(word)-1,-1,-1):
                c = word[i]
                if c not in p.children:
                    p.children[c] = TrieNode(c)
                p = p.children[c]
                p.accept = p.accept or (i == 0)
        self.stream = None

    def query(self, letter: str) -> bool:
        s = StreamNode(letter)
        s.next = self.stream
        self.stream = s
        p = self.trie
        i = 0
        accept = False
        while s != None and i < self.maxlen:
            if s.char not in p.children:
                return False
            p = p.children[s.char]
            if p.accept:
                return True
            s = s.next
            i += 1
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
