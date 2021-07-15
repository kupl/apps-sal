class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.waitlist = []
        for word in words:
            node = self.root
            for ch in word:
                node = node.child[ch]
            
            node.child['#'] = defaultdict(TrieNode)

    def query(self, letter: str) -> bool:
        waitlist = []
        now = self.root
        if letter in now.child:
            waitlist.append(now.child[letter])

        for node in self.waitlist:
            if letter in node.child:
                waitlist.append(node.child[letter])
                
        self.waitlist = waitlist
        for node in waitlist:
            if '#' in node.child:
                return True
            
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

