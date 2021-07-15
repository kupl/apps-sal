class Node:
    def __init__(self, char, parent):
        self.children = [None for _ in range(26)]
        self.char = char
        self.parent = parent
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.map = {}
        self.root = Node(' ', None)
        self.buffer = deque()
        self.max_size = max([len(word) for word in words])
        self.add(words)
    
    def add(self, words):
        for word in words:
            curr = self.root
            for c in word:
                if not curr.children[ord(c) - ord('a')]:
                    curr.children[ord(c) - ord('a')] = Node(c, curr)
                curr = curr.children[ord(c) - ord('a')]
            if word[-1] not in self.map:
                self.map[word[-1]] = []
            self.map[word[-1]].append(curr)

    def query(self, letter: str) -> bool:
        self.buffer.append(letter)
        if len(self.buffer) > self.max_size:
            self.buffer.popleft()
        if letter not in self.map:
            return False
        for node in self.map[letter]:
            curr = node
            for i in range(len(self.buffer) - 2, -1, -1):
                if curr is not self.root and curr.parent.char == self.buffer[i]:
                    curr = curr.parent
                else:
                    break
            if curr.parent is self.root:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

