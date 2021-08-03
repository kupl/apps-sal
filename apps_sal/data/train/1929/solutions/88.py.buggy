class Trie:
    def __init__(self, c: str, is_word: bool):
        self.c = c
        self.next_chars = {}
        self.is_word = is_word 
    def traverse(self, c):
        if c in self.next_chars:
            return self.next_chars[c]
        return None

    def add(self, c, is_word):
        if c not in self.next_chars:
            self.next_chars[c] = Trie(c, is_word)
        return self.next_chars[c]
    
class StreamChecker:
            
    def __init__(self, words: List[str]):
        self.tr = Trie(\"\", False)
        self.iters = []
        
        for word in words:
            cur = self.tr
            for c in word[::-1]:
                cur = cur.add(c, False)
            cur.is_word = True

    def query(self, letter: str) -> bool:
        self.iters.append(letter)
        cur = self.tr
        for c in self.iters[::-1]:
            cur = cur.traverse(c)
            if not cur:
                return False
            if cur.is_word:
                return True
            
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
