def vowelprune(w):
    vowels={'a','e','i','o','u'}
    r=''
    for i in w:
        if i in vowels:r+='*'
        else:r+=i
    return r
def check(vow,se,fir,word):
    
    if word in se:return word
    word=word.lower()
    if word in fir:return fir[word]
    l=len(word)
    word=vowelprune(word)
    if word in vow:return vow[word]
    return \"\"
class Solution:
    def spellchecker(self, w: List[str], q: List[str]) -> List[str]:
        se=set(w)
        fir={}
        vow={}
        for i in w:
            z=i
            i=i.lower()
            if i not in fir:
                fir[i]=z
            j=vowelprune(i)
            if j not in vow:
                vow[j]=z
        res=[]
        for i in q:
            res.append(check(vow,se,fir,i))
        return res
