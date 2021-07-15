class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie={}
        
        for word in set(words):
            node=self.trie
            for c in word[::-1]:
                node=node.setdefault(c,{})
            node['$']=word
        self.nodelist=[]
    def query(self, letter: str) -> bool:
        self.nodelist.insert(0,letter)
    
        node = self.trie
        for ch in self.nodelist:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

