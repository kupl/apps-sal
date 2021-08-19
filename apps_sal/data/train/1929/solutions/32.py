class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            root = self.trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]

            root['*'] = True
        self.storech = []

    def query(self, letter: str) -> bool:
        a = False
        storech = []
        if letter in self.trie:
            storech.append(self.trie[letter])
        for ele in self.storech:
            if letter in ele:
                storech.append(ele[letter])
        self.storech = storech
        return any('*' in ele for ele in self.storech)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
