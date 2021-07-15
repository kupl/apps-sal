class Tire:
    def __init__(self, char):
        self.char = char
        self.end = False 
        self.children = {} 
        
    def __repr__(self):
        return '<{}: {}>'.format(self.char, self.end)

class StreamChecker:

    def __init__(self, words: List[str]):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

        # self.root = Tire('^')
        # 
        # for word in words:
        #     node = self.root
        #     for char in word:
        #         if char not in node.children:
        #             node.children[char] = Tire(char)
        #         node = node.children[char]
        #     node.end = True    
        #     
        # self.possible_nodes = set() 

    def query(self, letter: str) -> bool:
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)
 
        # self.possible_nodes.add(self.root)
        # 
        # nxt = set()
        # found = False
        # for node in self.possible_nodes:
        #     if letter in node.children:
        #         nxt.add(node.children[letter])
        #         if node.children[letter].end:
        #             found = True
        # self.possible_nodes = nxt
        # return found
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
