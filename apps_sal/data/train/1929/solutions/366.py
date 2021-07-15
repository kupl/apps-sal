class StreamChecker:

    def __init__(self, words: List[str]):
        self.tries = {}
        self.hist = ''
        for word in words:
            cur = self.tries            
            for c in word[::-1]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = word
        print((self.tries))

    def query(self, letter: str) -> bool:
        self.hist += letter
        cur = self.tries
        for c in self.hist[::-1]:
            if '#' in cur:
                return True
            if c in cur:
                cur = cur[c]
            else:
                return False
        return '#' in cur

    
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

