class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ss = \"qwertyuiopasdfghjklzxcvbnm\"
        alltime = {}
        for i in ss:
            alltime[i] = 0
    
        def freq(s):
            temp = alltime.copy()
            for i in s:
                temp[i] += 1
            return temp
        
        a1 = []
        for i in A:
            a1.append(freq(i))
        
        a2 = []
        for i in B:
            a2.append(freq(i))
        
        for i in alltime:
            tt = 0
            for j in a2:
                tt = max(tt,j[i])
            alltime[i] = tt
        
        ans = []
        for i in range(len(a1)):
            flag = 0
            for j in alltime:
                if alltime[j] > a1[i][j]:
                    flag = 1
                    break
            if flag == 0:
                ans.append(A[i])
        return ans
