class StreamChecker:
    def __init__(self, words: List[str]):
        from collections import deque
        self.stream = deque()
        self.trie = {\"_\": False}
        self.max_stream_size = 0
        for word in words:
            self.max_stream_size = max(self.max_stream_size, len(word))
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {\"_\": False}
                node = node[char]
            node[\"_\"] = True
        #print(self.trie)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_stream_size:
            self.stream.popleft()
        
        node = self.trie
        #print(node)
        #print(self.stream)
        for idx in range(len(self.stream)-1, -1, -1):
            if node[\"_\"]:
                return True
            char = self.stream[idx]
            if char not in node:
                return node[\"_\"]
            node = node[char]
        #print(self.stream)
        return node[\"_\"]


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
