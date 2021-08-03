class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d={}
        t=set()
        for o in orders:
            if o[2] in d:
                d[o[2]].append(o[0])
            else:
                d[o[2]]=[o[0]]
                
        for o in orders:
            t.add(int(o[1]))
        dictionary_items = d.items()
        dd = sorted(dictionary_items)
        
        t=sorted(t)
        ans=[[\"Table\"]]
        
        m={}
        for o in orders:
            if o[1] in m:
                m[o[1]].append(o[2])
            else:
                m[o[1]]=[o[2]]
        
        for k,v in dd:
            ans[0].append(k)
            
        for k in t:
            ans.append([str(k)])
        
        for l in range(1,len(t)+1): # 1 -> table nums
            for y in range(1,len(ans[0])): # 0 -> food num
                ans[l].append(str(m[ans[l][0]].count(ans[0][y])))
            
        return ans
            
            
            
