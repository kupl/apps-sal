class StreamChecker:
    letter_queue = \"\"
    def __init__(self, words: List[str]):
        self.words_dict = {}
        for w in words:

            if w[-1] in self.words_dict:
                self.words_dict[w[-1]].add(w)
            else:
                self.words_dict[w[-1]] = set()
                self.words_dict[w[-1]].add(w)
        print(self.words_dict)
        
    def query(self, letter: str) -> bool:
        self.letter_queue += letter
        if letter in self.words_dict:
            for item in self.words_dict[letter]:
                # b = False
                l = len(item)
                if item == self.letter_queue[-l:]:
                    return True
                # if not b: return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
