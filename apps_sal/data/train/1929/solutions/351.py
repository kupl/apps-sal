from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        self.helper = defaultdict(list)
        for i in words:
            self.helper[i[-1]].append(i)
        self.characters = \"\"

    def query(self, letter: str) -> bool:
        self.characters += letter
        if letter in self.helper:
            for j in self.helper[letter]:
                if self.characters[-len(j):] == j: return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
