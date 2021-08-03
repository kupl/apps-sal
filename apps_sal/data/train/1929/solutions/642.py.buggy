class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = \"\"
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = '$'

    def query(self, letter: str) -> bool:
        self.letters += letter
        node = self.trie
        for ch in self.letters[::-1]:
            if ch not in node:
                return False
            node = node[ch]
            if '$' in node:
                return True
            
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
