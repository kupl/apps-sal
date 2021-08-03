# build a trie for sure.
# think about the reverse word (aka the order trie is queried is reverse) here, seems we have to build it in reverse order ??

class StreamChecker:
    def __init__(self, words: List[str]):
        
        self.map = dict()
        self.max_len = max([len(i) for i in words])
        self.history = \"\"
        
        for word in words:
            node = self.map
            for letter in word[::-1]:
                if letter not in node:
                    node[letter] = dict()
                node = node[letter]
            node['$'] = {}
            
    def query(self, letter: str) -> bool:
        self.history += letter
        node = self.map
        
        for l in self.history[::-1]:
            if l not in node: 
                return False
            node = node[l]
            if '$' in node:
                return True
        return False
            

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
