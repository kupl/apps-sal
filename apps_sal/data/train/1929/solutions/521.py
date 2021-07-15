class StreamChecker:

    def __init__(self, words: List[str]):
        self.dictionary = {}
        for word in words:
            last_letter = word[-1]
            if last_letter not in self.dictionary:
                self.dictionary[last_letter] = [word]            
            else:
                self.dictionary[last_letter].append(word)
        self.queries =''
            
    def query(self, letter: str) -> bool:
        self.queries += letter
        if letter not in self.dictionary:
            return False
        else:
            for word in self.dictionary[letter]:
                length = len(word)
                if self.queries[-length:] == word:
                    return True
            return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

