class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = \"\"
        # Build a trie
        self.map = {}
        for word in words:
            curr_node = self.map
            for letter in word[::-1]:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]
            curr_node['#'] = {}

    def query(self, letter: str) -> bool:
        \"\"\"Return true if letter completes a word in words.\"\"\"
        self.history += letter
        curr_node = self.map
        for char in self.history[::-1]:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
            if '#' in curr_node:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
