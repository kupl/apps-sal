class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = {}
        self.waiting = []

    def query(self, letter):
        \"\"\"
        :type letter: str
        :rtype: bool
        \"\"\"
        # self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        waiting = []
        for node in self.waiting + [self.trie]:
            if letter in node:
                waiting.append(node[letter])
        self.waiting = waiting
        return any('#' in node for node in self.waiting)
                


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
