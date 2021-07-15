class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        kns = defaultdict(list)
        
        for i, k1 in enumerate(keyName):
            tok = keyTime[i].split(':')
            mins =  int(tok[0]) * 60 + int(tok[1])
            if k1 not in kns:
                kns[k1] = [mins]
            else:
                kns[k1].append(mins)
                
        def getAlert(tl):
            start, count = 0, 1
            
            for i in range(1, len(tl)):
                print((tl[i], tl[start]))
                
                if tl[i] >= tl[start]:
 
                    if (tl[i] - tl[start]) <= 60:
                        count += 1
                    else:
                        while (tl[i] - tl[start]) > 60:
                            start += 1
                            
                        if start == i:
                            count = 1
                        else:
                            count = 2
                else:
                    start = i
                    count = 1                    

                if count >= 3:
                    return True            
            return False
        
        ans = []
        for k1, v1 in list(kns.items()):
            v = sorted(v1)
            al = getAlert(v)
            if al:
                ans.append(k1)

        return sorted(ans)
                    
                    
                
                
                
                    
            

