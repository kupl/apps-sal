from collections import deque   
class TrieNode:
    def __init__(self):
        self.children, self.end_node = {}, 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
     
class StreamChecker:
    ## trie, reverse?
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.Stream = deque()
        for word in words:
            self.trie.insert(word[::-1])
        # self.arr = [0] * 26
        # for word in words:
        #     # for l in word:
        #     self.arr[ord(word[-1])-ord('a')] += 1

    def query(self, letter: str) -> bool:
        # res = self.arr[ord(letter) - ord('a')] > 0
        # self.arr[ord(letter) - ord('a')] -= 1
        # return res
        self.Stream.appendleft(letter)
        cur = self.trie.root
        for c in self.Stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node == 1:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

