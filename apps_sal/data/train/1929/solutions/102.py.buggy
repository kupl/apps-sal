class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = defaultdict(dict)
        for word in words:
            cur = self.trie
            for letter in word:
                if letter not in cur: cur[letter] = {}
                cur = cur[letter]
            cur[\"#\"] = True
        self.point = deque()
        
    def query(self, letter: str) -> bool:
        temp = deque()
        self.point.append(self.trie)
        for pt in self.point:
            if letter in pt:
                temp.append(pt[letter])
        self.point = temp
        
        for pt in self.point:
            if \"#\" in pt:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
