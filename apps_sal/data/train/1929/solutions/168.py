class TrieNode:
    def __init__(self):
        self.arr = [None] * 26
        self.isWord = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.rt = TrieNode()
        self.S = \"\"
        self.mx = float('-inf')
        for w in words:
            node = self.rt
            for ch in w[::-1]:
                if node.arr[ord(ch) - ord('a')] is None:
                    node.arr[ord(ch) - ord('a')] = TrieNode()
                node = node.arr[ord(ch) - ord('a')]
            node.isWord = True
            self.mx = max(self.mx, len(w))

    def query(self, letter: str) -> bool:
        self.S = (letter + self.S)[:self.mx]
        node = self.rt
        for ch in self.S:
            if node.arr[ord(ch) - ord('a')] is None:
                return False
            node = node.arr[ord(ch) - ord('a')]
            if node.isWord:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
