class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #dict mapping
        #insert pattern into dict
        pattern_map = dict()
        for el in pattern:
            pattern_map[el] = 1
            
        res = []
        #seen = set()
        for word in words:
            #reset dict and seen for each new word
            #shallow copy
            pattern_map_dupe = copy.copy(pattern_map) 
            seen = set()
            if len(word) == len(pattern):
                i = 0
                for charw, charp in zip(word, pattern):
                    print(\"w: \", charw, \"p: \", charp)
                    print(pattern_map_dupe)
                    #subsequent encounter
                    if charw in seen:
                        if pattern_map_dupe[charp] != charw:
                            break
                    
                    #first encounter
                    #also must not be in seen already
                    elif pattern_map_dupe.get(charp, 0) == 1:
                        #don't want a=c, b=c
                        #must be one-to-one: a=a, b=c
                        if charw in seen:
                            break
                        else:
                            seen.add(charw)
                            pattern_map_dupe[charp] = charw
                    
                    #no match
                    else:
                        continue
                    i += 1

                if i == len(pattern):
                    res.append(word)
        return res
                    
        
