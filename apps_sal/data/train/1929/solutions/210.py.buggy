class StreamChecker:
    from collections import deque
    def __init__(self, words: List[str]):
        self.trie = dict()
        maxlen = 0
        #d = self.trie 
        for word in words:
            maxlen = max(maxlen,len(words))
            d = self.trie
            for i in range(len(word)-1, -1, -1):
                if word[i] not in d:
                    d[word[i]] = dict()
                d = d[word[i]]
            d[\"#\"]=dict()
        self.maxlen = maxlen
        #print(self.trie)
        self.history = deque([])
        

    def query(self, letter: str) -> bool:
        self.history.appendleft(letter)
        if len(self.history)>self.maxlen:
            self.history.pop()
        d = self.trie
        #print(self.history)
        for l in range(len(self.history)):
            #print(letter,self.history[l])
            if self.history[l] in d:
                d = d[self.history[l]]
                if \"#\" in d:
                    return True
            else:
                return False
                
                
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
