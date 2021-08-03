class Node:
    def __init__(self):
        self.kids = defaultdict(Node)
        self.words = []
class Trie:
    def __init__(self):
        self.head = Node()
        self.cache = defaultdict(str)
        self.exacts = defaultdict(str)
        self.novowels = defaultdict(str)
        self.time = 0
        self.sortkey = {}
                
    def novo(self, word):
        grp = list(word)
        for i,g in enumerate(grp):
            if g.lower() in 'aeiou':
                grp[i] = '*'
            else:
                grp[i] = grp[i].lower()
        return ''.join(grp)

    def add(self, word):
        curr = self.head
        if word.lower() not in self.cache:
            self.cache[word.lower()] = word
            
        self.exacts[word] = word

        nvwl = self.novo(word)
        if nvwl not in self.novowels:            
            self.novowels[nvwl] = word
        
        
    def search(self, word, start=None):
                    
        if word in self.exacts and start is None:
            return word
        lowered = word.lower()
        if lowered in self.cache and start is None:
            return self.cache[lowered]
        novowels = self.novo(word)
        if novowels in self.novowels and start is None:
            # print(word, novo(word), self.novowels[self.novo(word)])
            return self.novowels[novowels]
        
        
        return \"\"

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        tree = Trie()
        
        for word in wordlist:
            tree.add(word)
            
        out = []
        for q in queries:
            res = tree.search(q)                            
            out.append(res)
        
        # print(out)
        return out
