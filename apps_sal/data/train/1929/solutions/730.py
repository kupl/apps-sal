class StreamChecker(object):
    \"\"\"
    Copy paste from Lee215 on discussions
    My code is still being built but lazy...
    Also found another good resource for backend sys design... I'm sorry...
    \"\"\"
    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)

class TrieNode:
    
    def __init__(self):
        self.word = False
        self.child = defaultdict(TrieNode)

class StreamChecker1:

    def __init__(self, words: List[str]):
        \"\"\"
        Took around 5 minutes for the approach...
        45 minutes for the implementation... 
        Also did some amazon and day dreaming... in the noon...
        Not sure if this will run... but very hopeful...
        \"\"\"
        self.trie = TrieNode()
        for w in words:
            itr = self.trie
            for ch in w: itr = itr.child[ch]
            itr.word = True
        self.pointers = collections.deque(self.trie.child.items())

    def query(self, letter: str) -> bool:
        found, lt_indices = False, []
        for i, pair in enumerate(self.pointers): 
            k, v = pair
            if k == letter: lt_indices.append(i)
        
        print(letter, lt_indices)
        for i in lt_indices:
            k, v = self.pointers[i]
            
            if v.word: found = True
                
            self.pointers.extend(v.child.items())
        
        cnt = 0
        for i in lt_indices: 
            del self.pointers[i - cnt]
            cnt += 1
        
        print(letter, self.pointers, found)
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
