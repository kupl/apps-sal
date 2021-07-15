from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.max_word_len = 0
        for word in words:
            node = self.trie
            for i in reversed(list(range(len(word)))):
                if word[i] not in node:
                    node[word[i]] = {}
                node = node[word[i]]
            node[True] = True
            self.max_word_len = max(self.max_word_len, len(word))
        self.queue = deque()
            

            
    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        if len(self.queue) > self.max_word_len:
            self.queue.pop()
            
        node = self.trie
        for char in self.queue:
            if True in node:
                return True
            if char not in node:
                return False
            node = node[char]
        return True in node

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


