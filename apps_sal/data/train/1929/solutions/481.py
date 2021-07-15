class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.maxLen = len(max(words, key=lambda s: (len(s), s)))
        self.queue = deque([])
        
    def query(self, letter: str) -> bool:
        
        if len(self.queue) >= self.maxLen:
            self.queue.popleft()
            
        self.queue.append(letter)
        
        # for i in range(len(self.queue)-1, -1, -1):
        if self.trie.findWord(self.trie.store, len(self.queue)-1, ''.join(self.queue)):
            return True
            
        return False
            
        

class Trie:
    def __init__(self, words):
        self.store = {}
        for w in words:
            self.insertWord(self.store, len(w)-1, w)
        
    def insertWord(self, trie, p, w):
        if p < 0:
            return

        if w[p] not in trie:
            trie[w[p]] = {}
            
        self.insertWord(trie[w[p]], p-1, w)

        if p == 0:
            trie[w[p]]['$'] = True
            
    def findWord(self, trie, p, w):
        if p < 0 or w[p] not in trie:
            return False
        
        if '$' in trie[w[p]]:
            return True
        
        isAvail = False
        
        if w[p] in trie:
            isAvail = self.findWord(trie[w[p]], p-1, w)
        
        return isAvail
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

