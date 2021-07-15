class StreamChecker:

    def __initv1__(self, words: List[str]):
        self.dictionary:Dict[int, List[str]] = {}
        for w in words:
            l:int = len(w)
            if l not in self.dictionary:
                self.dictionary[l] = []
            self.dictionary[l].append(w)
            
        self.l:List[int] = sorted(self.dictionary.keys())
            
        print(self.l)
            
        
            
    def __init__(self, words: List[str]):
        self.dictionary:Dict[str, List[str]] = {}
        
        for w in words:
            if w[-1] in self.dictionary.keys():
                self.dictionary[w[-1]].append(w)
            else:
                self.dictionary[w[-1]] = [w]
                
        print(self.dictionary)
                
        self.word:str = \"\"

    def query(self, letter: str) -> bool:
        self.word += letter
        
        if letter in self.dictionary:
            for w in self.dictionary[letter]:
                l:int = len(w)
                if len(self.word) >= l and w == self.word[-l:]:
                    return True
            
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
