class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        dn = []
        for o in orders:
            if o[2] not in dn:
                dn.append(o[2])
                
            if o[1] in d:
                if o[2] in d[o[1]]:
                    d[o[1]][o[2]] += 1
                else:
                    d[o[1]][o[2]] = 1
            else:
                d[o[1]] = {}
                d[o[1]][o[2]] = 1
             
        dn.sort()
        fr = ['Table']
        for n in dn:
            fr.append(n)
        ans = [fr]
        st = list(d.keys())
        st.sort(key=lambda x:int(x))
        for t in st:
            r = [t]
            for n in dn:
                if n in d[t]:
                    r.append(str(d[t][n]))
                else:
                    r.append('0')
            ans.append(r)
        
        return ans
                

