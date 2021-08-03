class StreamChecker:

    def __init__(self, words: List[str]):
        self.word_buf = []
        self.wordDict = {}
        for w in words:
            temp_dict = self.wordDict
            for c in w:
                temp_dict = temp_dict.setdefault(c, dict())
            temp_dict[\"EOS\"] = \"EOS\"
        
    def query(self, letter: str) -> bool:
        waitlist = []
        # if letter can be the prefix of word
        if letter in self.wordDict:
            waitlist.append(self.wordDict[letter])
        # for each possible prefix, append letter if the new substr still can be a prefix
        for item in self.word_buf:
            if letter in item:
                waitlist.append(item[letter])
                
        self.word_buf = waitlist
        return any('EOS' in item for item in self.word_buf)
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
