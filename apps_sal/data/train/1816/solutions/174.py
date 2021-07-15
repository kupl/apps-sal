class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def def_val():
            return []
        d=defaultdict(def_val)
        n=len(keyName)
        for i in range(n):
            d[keyName[i]].append(keyTime[i])
        res=[]
        for i in d:
            arr=sorted(d[i])
            # print(i,arr)
            m=len(arr)
            if m>=3:
                for j in range(m-2):
                    [eh,em]=[int(k) for k in arr[j+2].split(\":\")]
                    [sh,sm]=[int(k) for k in arr[j].split(\":\")]
                    if eh*60+em-(sh*60+sm)<=60:
                        res.append(i)
                        break
        return sorted(res)
