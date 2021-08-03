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
        
    def add(self, word):
        curr = self.head
        if word.lower() not in self.cache:
            self.cache[word.lower()] = word
        self.exacts[word] = word
        
        def novo(word):
            grp = list(word)
            for i,g in enumerate(grp):
                if g.lower() in 'aeiou':
                    grp[i] = '*'
                else:
                    grp[i] = grp[i].lower()
            return ''.join(grp)
        
        nvwl = novo(word)
        if nvwl not in self.novowels:
            print(nvwl, word)
            self.novowels[nvwl] = word
        
        self.time += 1
        self.sortkey[word] = self.time
        temp = word.lower()
        for w in temp:
            curr = curr.kids[w]
        
        curr.words.append(word)
        
    def search(self, word, start=None):
        def novo(word):
            grp = list(word)
            for i,g in enumerate(grp):
                if g.lower() in 'aeiou':
                    grp[i] = '*'
                else:
                    grp[i] = grp[i].lower()
                    
            return ''.join(grp)
                    
        if word in self.exacts and start is None:
            return word
        if word.lower() in self.cache and start is None:
            return self.cache[word.lower()]
        if novo(word) in self.novowels and start is None:
            print(word, novo(word), self.novowels[novo(word)])
            return self.novowels[novo(word)]
        # print(self.novowels)
        
        if start is None:
            start = self.head
        if word == \"vavkmj\":
            print(\"search.word\", word, [k for k in start.kids['v'].kids.keys()])     
        curr = start

        
        for i,w in enumerate(word):
            if w.lower() in 'aeiou':
                res = []
                for c in curr.kids.keys():
                    if c in 'aeiou':
                        out = self.search(word[i+1:], curr.kids[c])
                        if out != \"\":
                            res.append(out)
                if res:
                    print(\"resss\", word, res)
                    res.sort(key=lambda x:self.sortkey[x])
                    
                    print(\"resss2\", word, res)
                    return res[0]
                return \"\"
            elif w in curr.kids:
                curr = curr.kids[w]
            elif w.lower() in curr.kids:
                curr = curr.kids[w.lower()]
            elif w.upper() in curr.kids:
                curr = curr.kids[w.upper()]
            else:
                break
                # assert(False)
                # if w.lower() in 'aeiou':
                #     if word == \"vavkmj\":
                #         print(curr.kids.keys())
                #     for c in curr.kids.keys():
                #         if c in 'aeiou':
                #             out = self.search(c+word[i+1:], curr)
                #             if out != \"\":
                #                 return out
                #     return \"\"
                # else:
                #     return \"\"
        # print(\"curr.words\",word, \"->\", curr.words)     
        if curr and curr.words:
            curr.words.sort(key=lambda x:self.sortkey[x])
            return curr.words[0]
        return \"\"
    

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        tree = Trie()
        
        for word in wordlist:
            tree.add(word)
            
        out = []
        for q in queries:
            res = tree.search(q)
            # print(q,\"->\", res)
            if res == \"\" and q and q[0].lower() in 'aeiou':
                for v in 'aeiou':
                    if q[0] != v:
                        res = tree.search(v+q[1:])
                        if res != \"\":
                            break
            # if q == \"aai\":
            #     print(q,\"->\", res)
            out.append(res)
        
        # print(out)
        return out
