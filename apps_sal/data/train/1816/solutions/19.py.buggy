class Solution:
    def gethourlater(self, time):
        hr = time[:time.index(\":\")]
        hr = int(hr)+1
        hr = str(hr)
        hr = hr if len(hr)==2 else \"0\"+hr
        return hr+time[time.index(\":\"):]
        
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        s = [(keyName[i], keyTime[i]) for i in range(n)]
        s.sort()
        
        ind = 0
        res = []
        while ind < len(s):
            name = s[ind][0]
            found = False
            start = ind
            while ind < len(s) and name == s[ind][0]:
                while start < len(s) and ind < len(s) and self.gethourlater(s[start][1]) < s[ind][1]:
                    start += 1
                if ind-start >= 2:
                    found = True
                ind += 1
            if (found): res += [name]
        return res
        
