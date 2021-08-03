class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for i, c in enumerate(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
                if i == len(word)-1:
                    node[\"#\"] = {}
        print(self.trie)        
        self.candidates = [self.trie]

    def query(self, letter: str) -> bool:
        new_candidates = [self.trie]
        word_found = False
        for node in self.candidates:
            if letter in node:
                new_candidates.append(node[letter])
                if \"#\" in node[letter]:
                    word_found = True
        self.candidates = new_candidates
        return word_found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
