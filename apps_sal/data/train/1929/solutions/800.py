class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.l=[]
        self.trie={}
        for word in words:
            self.insert(word)
        
        print(self.trie)
    
    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        start = self.trie
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True
                    

    def query(self, letter: str) -> bool:
        
        t=self.trie
        ans=False
        temp=[]
        for d in self.l:
            if letter in d:
                if \"$\" in d[letter]:
                    ans=True
                temp.append(d[letter])
        
        self.l=temp
        if letter in t:
            self.l.append(t[letter])
            if \"$\" in t[letter]:
                return True
        
        return ans
                
# param_1 = obj.query(letter)
