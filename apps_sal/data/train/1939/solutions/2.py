

class Trie:
    def __init__(self):        
        self.cache = defaultdict(str)
        self.exacts = defaultdict(str)
        self.novowels = defaultdict(str)
        self.vowels = set('aeiou')
                
    def novo(self, word):
        word = word.lower()
        grp = list(word)
        for i,g in enumerate(grp):
            if g in self.vowels:
                grp[i] = '*'
        out = ''.join(grp)
        return out

    def add(self, word):    
        lowered = word.lower()
        if lowered not in self.cache:
            self.cache[lowered] = word
            
        self.exacts[word] = word

        nvwl = self.novo(word)
        if nvwl not in self.novowels:            
            self.novowels[nvwl] = word
        
        
    def search(self, word):                    
        if word in self.exacts:
            return word
        
        lowered = word.lower()
        if lowered in self.cache:
            return self.cache[lowered]
        
        novowels = self.novo(word)
        if novowels in self.novowels:
            # print(word, novo(word), self.novowels[self.novo(word)])
            return self.novowels[novowels]
        
        
        return \"\"

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        tree = Trie()
        
        for word in wordlist:
            tree.add(word)
            
        # out = []
        # for q in queries:
        #     res = tree.search(q)                            
        #     out.append(res)
        
        # print(out)
        return [tree.search(q) for q in queries]
