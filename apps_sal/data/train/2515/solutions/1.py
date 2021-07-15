class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowels = set(['a','e','i','o','u'])
        s = ''
        for i,item in enumerate(S.strip().split()):
            if item[0].lower() in vowels:
                s+=item
            else:
                s+=item[1:]+item[0]
            
            s+='ma'+'a'*(i+1)+' '
        
        return s[:-1]
