class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = \"\"
        for word in words:
            curr = self.trie
            for w in word[::-1]:
                curr = curr.setdefault(w,{})
            curr['$'] = '$'
    def query(self, letter: str) -> bool:
        self.stream += letter
        curr = self.trie
        for s in self.stream[::-1]:
            if '$' in curr: return True
            if s not in curr: return False
            curr = curr[s]
        return '$' in curr
            

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
