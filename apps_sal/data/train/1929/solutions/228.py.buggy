from collections import deque
from typing import Dict

class Trie:
    def __init__(self):
        self.d = {}
    
    def ends(self) -> bool:
        return \"$\" in self.d
    
    def absent(self, c) -> bool:
        return c not in self.d
    
    def getTrie(self, c):
        return self.d[c]
    
    def addWord(self, word: str) -> None:
        if not word:
            self.d[\"$\"] = None
            return
        if word[0] not in self.d:
            self.d[word[0]] = Trie()
        self.d[word[0]].addWord(word[1:])

class StreamChecker:

    def __init__(self, words: List[str]):
        self.max_len = max(map(len, words))
        self.suffix_trie = self.build_tree(words)
        self.queue = deque([])
    
    def build_tree(self, words: List[str]) -> Dict[str, Trie]:
        trie: Trie = Trie()
        for word in words:
            trie.addWord(word[::-1])
        return trie

    def query(self, letter: str) -> bool:
        # if self.max_len == self.curr_len:
        #     self.queue.popleft()
        self.queue.appendleft(letter)
        i = 0
        n = self.suffix_trie
        while i < len(self.queue):
            if n.ends():
                return True
            if n.absent(self.queue[i]):
                return False
            n = n.getTrie(self.queue[i])
            i += 1
        return n.ends()
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
