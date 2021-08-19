class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            temp = self.trie
            for char in word:
                if char not in temp:
                    temp[char] = {}
                temp = temp[char]
            temp['*'] = True
        self.pointer = deque()

    def query(self, letter: str) -> bool:
        temp = self.trie
        self.pointer.append(temp)
        length = len(self.pointer)
        flag = False
        for i in range(length):
            node = self.pointer.popleft()
            if letter in node:
                node = node[letter]
                self.pointer.append(node)
                if '*' in node:
                    flag = True
        return flag


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
