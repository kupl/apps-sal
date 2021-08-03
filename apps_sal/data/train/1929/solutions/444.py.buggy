class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = \"\"
        self.dictionary = {}
        for word in words:
            location = self.dictionary
            for char in word[::-1]:
                if char not in location:
                    location[char] = {}
                location = location[char]
            location[\"goodbye\"] = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        count = -1
        location = self.dictionary
        for char in self.stream[::-1]:
            if char in location:
                location = location[char]
                if \"goodbye\" in location:
                    return True
                continue
            return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
