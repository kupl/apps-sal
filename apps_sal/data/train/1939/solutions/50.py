class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_ori = {}
        words_cap = {}
        words_vowel = {}
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        
        def gen_vowel(cur, val, pos):
            if pos >= len(cur):
                return
            if cur[pos] in vowel:
                for i in vowel:
                    if i != cur[pos]:
                        key = (cur[0:pos] + i + cur[pos+1:]).lower()
                        try:
                            if words_vowel[key]:
                                continue
                        except:
                            words_vowel[key] = val
                        gen_vowel(key, val, pos+1)
            gen_vowel(cur, val, pos+1)
        
        for i in wordlist:
            words_ori[i] = i
            temp = i[:]
            gen_vowel(temp, i, 0)
            try:
                if words_cap[temp.lower()]:
                    continue
            except:
                temp = temp.lower()
                words_cap[temp] = i
                
        # print(words_ori, words_cap, words_vowel)
        
        ans = []
        for i in queries:
            try:
                if words_ori[i]:
                    ans.append(i)
                    continue
            except: pass
            
            try:
                if words_cap[i.lower()]:
                    ans.append(words_cap[i.lower()])
                    continue
            except: pass
            
            try:
                if words_vowel[i.lower()]:
                    ans.append(words_vowel[i.lower()])
                    continue
            except: pass
            
            ans.append(\"\")

        return ans
                
