class StreamChecker:
    from collections import deque

    def __init__(self, words: List[str]):
        self.max = len(max(words, key=len))
        self.words = tuple(words)
        self.letters = deque(maxlen=self.max)

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        l = ''.join(self.letters)
        return l.endswith(self.words)

    '''
    def __init__(self, words: List[str]):
        self.words = set(words)
        self.letters = ''
        self.fragments = {}
        for w in words:
            temp = self.fragments
            for i in range(len(w)):
                sec = w[len(w)-1-i:]
                if sec not in temp:
                    temp[sec] = {}
                temp = temp[sec]
                    
    def query(self, letter: str) -> bool:
        self.letters += letter
        chars = self.letters
        
        temp = self.fragments
        for i in range(len(chars)):
            sec = chars[len(chars) - 1 - i:]
            if sec in self.words:
                return True
            if sec not in temp:
                return False
            temp = temp[sec]
    '''
    '''
    def __init__(self, words: List[str]):
        self.words = tuple(words)
        self.letters = ''
        
    def query(self, letter: str) -> bool:
        self.letters +=letter
        return self.letters.endswith(self.words)        
    '''
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
