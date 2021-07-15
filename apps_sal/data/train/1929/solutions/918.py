class StreamChecker:

    def __init__(self, words: List[str]):
        self.Dict = collections.defaultdict(set)
        self.queries = ''
        for word in words:
            self.Dict[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        if letter not in self.Dict:
            self.queries += letter
            return False
        else:
            temp = set([len(x) for x in self.Dict[letter]])
            self.queries += letter
            for length in temp:
                if (length <= len(self.queries)) and (self.queries[-1:-length-1:-1][::-1] in self.Dict[letter]):
                    return True
                

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

