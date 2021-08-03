class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = {}
        self.word = \"\"
        for i in range(len(words)):
            lastChar = words[i][-1]
            if lastChar in self.dict:
                self.dict[lastChar].append(words[i])
            else:
                self.dict[lastChar] = [words[i]]
        #print (self.dict)  

    def query(self, letter: str) -> bool:      
        self.word += letter
        count = len(self.word) 
        if letter in self.dict:
            if letter in self.dict[letter]:
                return True
            else:
                lWords = list(self.dict[letter])                 
                for i in range(len(lWords)):
                    length = len(lWords[i])
                    #print (letter, self.word, self.word[count-length:], lWords[i])
                    if count >= length and self.word[count-length:] == lWords[i]:
                        #print (letter, lWords[i])
                        return True
       
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
