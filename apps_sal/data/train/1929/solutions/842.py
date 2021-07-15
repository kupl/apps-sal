class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.head = TrieNode()
        for word in words:
            p = self.head
            for c in word:
                p = p.children[c]
            p.isWord = True
        self.pos = [self.head]
        
    def query(self, letter: str) -> bool:
        tmp = [self.head]
        is_word = False
        for p in self.pos:
            if letter in p.children:
                nxt = p.children[letter]
                tmp.append(nxt)
                if nxt.isWord:
                    is_word = True
        self.pos = tmp
        return is_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

