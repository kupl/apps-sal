class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        vowels = set('aeiou')
        
        # Map lowercase words to word
        w = collections.defaultdict(list)
        for word in wordlist:
            w[word.lower()].append(word)
            
        # Map (vowel_count, len_word) to lowercase vowel-less words : word
        v = collections.defaultdict(list)
        vl = collections.defaultdict(list)
        for k in w:
            vowel_less = ''.join(char for char in k if char not in vowels)
            v[(len(vowel_less), len(k))].append(vowel_less)
            vl[vowel_less].append(k)
        
        res = []
        for q in queries:
            
            # 1. Case sensitive check
            k = q.lower()
            if k in w:
                res.append(q if (q in w[k]) else w[k][0])
                continue
                
            # 2. Vowel check
            vowel_less = ''.join(char for char in k if char not in vowels)
            if vowel_less in v[(len(vowel_less), len(k))]:
                for word in vl[vowel_less]:
                    if len(word) == len(k):
                        for a,b in zip(word,k):
                            if (a in vowels) != (b in vowels):
                                break
                        else:
                            res.append(w[word][0])
                            break
                else:
                    res.append(\"\")
            else:
                res.append(\"\")
        
        return res
