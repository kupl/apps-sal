from collections import deque

class StreamChecker:
    TERMINAL = None

    def __init__(self, words: List[str]):
        self.trie = {}
        self.build_trie(words)
        self.cursors = deque([])
        
    def build_trie(self, words: List[str]):
        trie = self.trie
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.TERMINAL] = True

    def query(self, letter: str) -> bool:
        cursors = self.cursors
        cursors.append(self.trie)
        found = False
        
        valid_cursors = []
        
        while cursors:
            cursor = cursors.popleft()
            if letter in cursor:
                cursor = cursor[letter]
                valid_cursors.append(cursor)
                if self.TERMINAL in cursor:
                    found = True
                    
        cursors.extend(valid_cursors)
                    
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

