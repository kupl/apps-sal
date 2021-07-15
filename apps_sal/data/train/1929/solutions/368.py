class StreamChecker:
    word=[]
    d={}
    queryseq=\"\"
    def __init__(self, words: List[str]):
        self.word=[]
        self.d={}
        self.queryseq=\"\"
        for i in range(len(words)):
            self.word.append(words[i])
            ch=words[i][-1]
            if ch in self.d:
                self.d[ch].append(i)
            else:
                self.d[ch]=[i]
        #print (self.d)

    def query(self, letter: str) -> bool:
        self.queryseq+=letter
        ch=letter[-1]
        if ch not in self.d:
            return False
        for i in self.d[ch]:
            x=self.word[i]
            if self.queryseq[-len(x):] ==x:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
