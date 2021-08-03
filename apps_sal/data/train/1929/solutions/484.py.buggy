class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {}
        for word in words:
            if word[-1] not in self.dic:
                self.dic[word[-1]] = [word[:-1]]
            else:
                self.dic[word[-1]].append(word[:-1])
        
        self.string = \"\"

    def query(self, letter: str) -> bool:
        self.string += letter
        if letter in self.dic:
            for word in self.dic[letter]:
                length = len(word) + 1
                complete_word = word + letter
                if len(self.string) >= length and complete_word == self.string[- length:]:
                    return True
            return False
        else:
            return False

