class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if cur.get('*'):
            return True
        return False
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max_len = 0
        words = list([s[::-1] for s in words])
        for word in words:
            self.max_len = max(self.max_len, len(word))
            self.trie.insert(word)
        self.query_store = deque(maxlen=self.max_len)
        

    def query(self, letter: str) -> bool:
        self.query_store.appendleft(letter)
        query = ''.join(self.query_store)
        cur = self.trie.head
        for ch in query:
            if ch not in cur:
                return False
            cur = cur[ch]
            if cur.get('*'):
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

