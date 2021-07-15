class StreamChecker:

    def __init__(self, words: List[str]):
        self.size = len(max(words, key=len))
        self.buffer = \"\"
        self.words = [word[::-1] for word in words]
        self.words.sort() 
        
    def query(self, letter: str) -> bool:
        print('Start\
')
        self.buffer += letter
        # self.buffer = self.buffer[-self.size:] # trim buffer
        
        for word in self.words:  
            buffer_strip = self.buffer[-len(word):]
            if word[::-1] == buffer_strip:
                return True
            if(word[0] > letter):
                return False


        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
