class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            node = self.trie
            for i in w:
                if i not in node:
                    node[i] = {}
                node = node[i]
            node[\"end\"] = True
        self.active = {\"\" : self.trie}

    def query(self, letter: str) -> bool:
        new_active = {}
        ret = False
        count = 0
        
        for a in self.active:
            node = self.active[a]
            if letter in node:
                node = node[letter]
                if \"end\" in node:
                    ret = True
                new_active[count] = node
                count += 1
        new_active[count] = self.trie
        self.active = new_active
        return ret

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
