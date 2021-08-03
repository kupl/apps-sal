class Solution:
    def spellchecker(self, wordlist,queries):
        
        def getWords(wordlist):
            
            dict = {}
            
            for i in range(len(wordlist)):
                
                if wordlist[i] not in dict:
                    
                    dict[wordlist[i]] = i
                    
            return dict
        
        def GetVowels(wordlist):
            
            dict = {}
            
            for i in range(len(wordlist)):
                
                word = GetWord(wordlist[i])
                
                if word not in dict:
                    
                    dict[word] = wordlist[i]
                    
            return dict
            
        
        def GetCapital(wordlist):
            
            dict = {}
            
            for i in range(len(wordlist)):
                
                if wordlist[i].lower() not in dict:
                    
                    dict[wordlist[i].lower()] = wordlist[i]
                    
            return dict
        
        def helper(dict,word,ret):
        
            make = GetWord(word)
            
            return ret + [\"\"] if make not in dict else ret + [dict[make]]
        
        def GetWord(word):
            
            vowels = {\"a\":0,\"e\":0,\"i\":0,\"o\":0,\"u\":0}
            word = word.lower()
            
            s = \"\"
            
            for i in range(len(word)):
                
                if word[i] in vowels:
                    
                    s += \"1\"
                    
                else:
                    
                    s += word[i]
                    
            return s
                    
        
        ret = []
        
        words = getWords(wordlist)
        vowels = GetVowels(wordlist)
        capital = GetCapital(wordlist)
        
        for i in range(len(queries)):
            
            if queries[i] in words:
                
                ret.append(queries[i])
                
            elif queries[i].lower() in capital:
                
                ret.append(capital[queries[i].lower()])
            
            else:
                
                ret = helper(vowels,queries[i],ret)
            
        return ret
        
