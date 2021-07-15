class StreamChecker:
    def __init__(self, words: List[str]):
        self.waitlist=[]
        self.trie=dict()
        for word in words:
            temp=self.trie
            for letter in word:
                temp=temp.setdefault(letter,dict())
            temp[\"%\"]=\"%\"
        print(self.trie)
        
    def query(self, letter: str) -> bool:
        wait=[]
        if letter in self.trie:
            wait.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                wait.append(item[letter])
        self.waitlist=wait
        return any(\"%\" in i for i in self.waitlist)
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
