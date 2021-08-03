class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {};
        for word in words:
            if word[-1] not in self.dic:
                self.dic[word[-1]] = [word[:-1]];
            else:
                self.dic[word[-1]].append(word[:-1]);
            self.s = \"\";
                                     
    def query(self, letter: str) -> bool:
        self.s += letter;
        if letter in self.dic:
            for word in self.dic[letter]:
                length = len(word) + 1;
                cw = word + letter;
                if len(self.s) >= length and cw == self.s[-length:]:
                    return True;
            return False;
        else:
            return False;


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
