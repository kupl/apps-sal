from collections import deque

class Trie:
    def __init__(self):
        self.last_nodes = {}

    def add(self, word):
        last_char = word[-1]
        word_len = len(word)
        if last_char in self.last_nodes:
            if word_len in self.last_nodes[last_char]:
                self.last_nodes[last_char][word_len].add(word)
            else:
                self.last_nodes[last_char][word_len] = set([word])
        else:
            self.last_nodes[last_char] = {word_len: set([word])}
    
    def smart_search(self, word):
        last_char = word[-1]
        if last_char in self.last_nodes:
            for word_len in range(1, len(word) + 1):
                if word_len in self.last_nodes[last_char] and\\
                        word[-word_len:] in self.last_nodes[last_char][word_len]:
                    return True
        return False
                    

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max_size = 0
        self.cache = deque()
        
        for word in words:
            self.trie.add(word)
            self.max_size = max(len(word), self.max_size)

    def query(self, letter: str) -> bool:
        self.cache.append(letter)
        if len(self.cache) > self.max_size:
            self.cache.popleft()

        return self.trie.smart_search(''.join(self.cache))
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
