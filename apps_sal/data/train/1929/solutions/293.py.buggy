class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = \"\"
        self.dict = collections.defaultdict(set)
        for i in words:
            self.dict[i[-1]].add(i)
            

    def query(self, letter: str) -> bool:
        self.letters += letter[0]
        return any(self.letters.endswith(word) for word in self.dict[letter])



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
