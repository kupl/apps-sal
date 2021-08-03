class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = {}
        for word in words:
            trieNode = self.Trie
            for ch in word[::-1]:
                if ch not in trieNode:
                    trieNode[ch] = {}
                trieNode = trieNode[ch]
            trieNode['END'] = True
        self.letter = ''

    def query(self, letter: str) -> bool:
        self.letter += letter
        trieNode = self.Trie
        for ch in self.letter[::-1]:
            if ch not in trieNode:
                return False
            trieNode = trieNode[ch]
            if 'END' in trieNode:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
