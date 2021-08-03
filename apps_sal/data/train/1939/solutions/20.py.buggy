class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_set=set(wordlist)
        
        vowelLookUp={
            
        }
        lowerLookUp={}
        
        vowels=[\"a\",\"e\",\"i\",\"o\",\"u\"]
        
        for word in wordlist:
            temp=\"\"
            lowercase=word.lower()
            if lowercase not in lowerLookUp:
                lowerLookUp[lowercase]=word
            for i in range(len(lowercase)):
                if lowercase[i] not in vowels:
                    temp+=lowercase[i]
                else:
                    temp+=\"*\"
            if temp not in vowelLookUp:
                vowelLookUp[temp]=word
        
        result=[]
        for query in queries:
            if query in words_set:
                result.append(query)
                continue
            elif query.lower() in lowerLookUp:
                result.append(lowerLookUp[query.lower()])
                continue
            masked_query=\"\"
            query=query.lower()
            for i in range(len(query)):
                if query[i] not in vowels:
                    masked_query+=query[i]
                else:
                    masked_query+=\"*\"
            if masked_query in  vowelLookUp:
                result.append(vowelLookUp[masked_query])
            else:
                result.append(\"\")
        return result
        
        
