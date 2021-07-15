class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        
        for word in words:
            current = self.trie
            for letter in word:
                current.setdefault(letter, {})
                current = current[letter]
            current[\"__end__\"] = word
        
        self.currents = []
    def query(self, letter: str) -> bool:
        
        self.currents.append(self.trie)
        
        ans = False
        new_currents = []
        for pos, current in enumerate(self.currents):
            if letter in current:
                new_currents.append(current[letter])
                if \"__end__\" in current[letter]:
                    ans = True
        self.currents = new_currents
        return ans

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
