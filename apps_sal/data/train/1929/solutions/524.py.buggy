class StreamChecker2:

    def __init__(self, words: List[str]):
        self.words = words
        self._m = set([])

    def query(self, letter: str) -> bool:
        exists = False
        updated_list = set([])
        for ind, word in enumerate(self.words):
            if letter == word:
                exists = True
            if letter == word[0] and len(word) > 1:
                updated_list.add((0, ind))
        for ind, wi in list(self._m):
            if letter == self.words[wi][ind+1:]:
                exists = True
            elif letter == self.words[wi][ind+1] and len(self.words[wi][ind+1:]) > 1:
                updated_list.add((ind+1, wi))
        self._m = updated_list
        return exists

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
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
