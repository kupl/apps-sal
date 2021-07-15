class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.end = '*'
        for word in words:
            self.insert(word[::-1])
        self.history = \"\"
        print(self.root)
    def query(self, letter: str) -> bool:
        self.history += letter
        return self.search(self.history[::-1])
            
        
    
    def insert(self, words:str) -> None:
        current = self.root
        for char in words:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end] = True
    
    def search(self, string:str) -> bool:
        current = self.root
        for char in string:
            if self.end in current:
                return True
            if char in current:
                current = current[char]
            else:
                return False
        return self.end in current
                

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
