class StreamChecker:

    def __init__(self, words: List[str]):
        
        import collections
        
        self.trie = dict()
        self.maxLen = 0
        
        for word in words:
            node = self.trie
            self.maxLen = max(self.maxLen, len(word))
            for w in (word[::-1] + \"*\"):
                if w not in node:
                    node[w] = dict()
                node = node[w]
                
        self.queue = collections.deque([], self.maxLen)

    def query(self, letter: str) -> bool:
        
        self.queue.append(letter)
        term = list(self.queue)
        term = term[::-1] + [\"*\"]
        i = 0
        node = self.trie
        
        while(i<len(term)):
            if \"*\" in node:
                return(True)
            elif term[i] not in node:
                return(False)
            else:
                node = node[term[i]]
                i += 1
                
        return(True)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
