class TrieNode:
    def __init__(self):
        self.children = {}
        self.found = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.term = \"\"
        for w in words:
            cur = self.root
            for c in w[::-1]:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.found = True

    def query(self, letter: str) -> bool:
        self.term += letter
        cur = self.root
        for c in self.term[::-1]:
            if cur.found:
                return True
            if c not in cur.children:
                break
            cur = cur.children[c]
        if cur.found:
            return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
