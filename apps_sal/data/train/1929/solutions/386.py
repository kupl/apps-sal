class StreamChecker:
    def __init__(self, words: List[str]):
        self.history = ''
        self.map = {}
        for word in words:
            curr_node = self.map
            for letter in word[::-1]:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]
            curr_node['#'] = {}

    def query(self, letter: str) -> bool:
        self.history += letter
        curr_node = self.map
        for l in self.history[::-1]:
            if l not in curr_node:
                return False
            curr_node = curr_node[l]
            if '#' in curr_node:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

