class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.query_buffered = \"\"
        for word in words:
            tmp = self.trie
            for w in word[::-1]:
                if w not in tmp:
                    tmp[w] = dict()
                    tmp = tmp[w]
                else:
                    tmp = tmp[w]
            tmp['#HasWord#'] = True
        
        

    def query(self, letter: str) -> bool:
        tmp = self.trie
        self.query_buffered += letter
        for c in self.query_buffered[::-1]:
            if \"#HasWord#\" in tmp:
                return True
            if c in tmp:
                tmp = tmp[c]
            else:
                return False
        return \"#HasWord#\" in tmp        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
