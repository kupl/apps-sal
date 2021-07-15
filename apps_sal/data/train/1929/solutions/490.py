class StreamChecker:

    def __init__(self, words: List[str]):
        self.d={}
        for i in words:
            if(i[-1] not in self.d):
                self.d[i[-1]]=[i[:-1]]
            else:
                self.d[i[-1]].append(i[:-1])
                
        self.s=''
    def query(self, letter: str) -> bool:
        self.s+=letter
        if letter in self.d:
            for i in self.d[letter]:
                word=i+letter
                if len(self.s)>=len(word) and word==self.s[-len(word):]:
                    return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

