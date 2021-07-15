class Node:
    
    def __init__(self, flag=False):
        self.flag = False
        self.a = [None] * 26
    
    def insert(self, s, p):
        if p == len(s):
            self.flag = True
            return
        c = ord(s[p]) - ord('a')
        if self.a[c] is None:
            self.a[c] = Node()
        self.a[c].insert(s, p + 1)
        
    def query(self, s, p):
        if p == -1:
            return False
        c = ord(s[p]) - ord('a')
        if self.a[c] is None:
            return False
        if self.a[c].flag:
            return True
        return self.a[c].query(s, p - 1)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.node = Node()
        self.s = []
        for word in words:
            self.node.insert(word[::-1], 0)

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        return self.node.query(self.s, len(self.s) - 1)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

