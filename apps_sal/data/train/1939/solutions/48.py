class Solution:

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        caps = {}
        vowels = {}
        setwordlist = set(wordlist)
        for i in wordlist:
            cap = i.lower()
            vowel = ''.join(['*' if x in 'aeiou' else x for x in i.lower()])
            if cap not in caps:
                caps[cap] = i
            if vowel not in vowels:
                vowels[vowel] = i
        print(caps, vowels)
        ans = []
        for i in queries:
            cap = i.lower()
            vowel = ''.join(['*' if x in 'aeiou' else x for x in i.lower()])
            if i in setwordlist:
                ans.append(i)
            elif cap in caps:
                for x in caps:
                    if x == cap:
                        ans.append(caps[x])
                        break
            elif vowel in vowels:
                for x in vowels:
                    if x == vowel:
                        ans.append(vowels[x])
                        break
            else:
                ans.append('')
        return ans
