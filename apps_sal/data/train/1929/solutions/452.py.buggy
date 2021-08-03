from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        self.dictionary = defaultdict(list)
        for word in words:
            self.dictionary[word[-1]].append(word[:-1])
        
        self.pastQueries = \"\"
        
    def query(self, letter: str) -> bool:
        self.pastQueries += letter
        if letter in self.dictionary:
            for word in self.dictionary[letter]:
                complete_word = word + letter
                length = len(complete_word)
                if len(self.pastQueries) >= length and complete_word == self.pastQueries[- length:]:
                    return True
            return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
