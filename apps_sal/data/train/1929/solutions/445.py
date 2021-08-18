class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = set(words)
        self.letters = ''
        self.fragments = {}
        for w in words:
            temp = self.fragments
            for i in range(len(w)):
                sec = w[len(w) - 1 - i:]
                if sec not in temp:
                    temp[sec] = {}
                temp = temp[sec]

    def query(self, letter: str) -> bool:
        self.letters += letter
        chars = self.letters

        temp = self.fragments
        for i in range(len(chars)):
            sec = chars[len(chars) - 1 - i:]
            if sec not in temp:
                return False
            temp = temp[sec]
            if sec in self.words:
                return True

    '''
    def __init__(self, words: List[str]):
        self.words = tuple(words)
        self.letters = ''
        
    def query(self, letter: str) -> bool:
        self.letters +=letter
        return self.letters.endswith(self.words)        
    '''
