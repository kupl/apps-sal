class TrieNode:
    def __init__ (self):
        self.children: Dict[str, TrieNode] = {}
    def __str__ (self):
        l = \"\"
        for s in self.children:
            l = l+s+\"[\"
            if self.children[s]:
                l = l+str(self.children[s])
            l = l+\"]\"
        return(l)


class ZStreamChecker:    
    
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            p = self.root
            for l in w:
                if l not in p.children:
                    p.children[l] = TrieNode()
                p = p.children[l]
        self.pointers = set()
        self.pointers.add(self.root)

    def query(self, letter: str) -> bool:
        ret = False
        newset = set()
        newset.add(self.root)
        for p in self.pointers:
            if letter in p.children:
                if p.children[letter].children=={}:
                    ret = True
                else:
                    newset.add(p.children[letter])
        self.pointers = newset
        return ret
                
class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
