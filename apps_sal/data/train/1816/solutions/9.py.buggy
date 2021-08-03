class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        res = set()

        for i in range(len(keyName)):
            if keyName[i] in d.keys():
                h = int(keyTime[i].split(\":\")[0])
                m = int(keyTime[i].split(\":\")[1])
                d[keyName[i]].append((h, m))
            else:
                d[keyName[i]] = []
                h = int(keyTime[i].split(\":\")[0])
                m = int(keyTime[i].split(\":\")[1])
                d[keyName[i]].append((h, m))
        for k, v in d.items():
            List.sort(v)

            for i in range(len(v)-2):
                (h0, m0) = v[i]
                (h1, m1) = v[i+2]
                if h1 - h0 <= 1:
                    if m1 <= m0 or h1 == h0:
                        res.add(k)
        res = list(res)
        List.sort(res)               
        return res
    
