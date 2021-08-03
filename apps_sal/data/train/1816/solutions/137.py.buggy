class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def count_time(s):
            l = s.split(':')
            return 60 * int(l[0]) + int(l[1])
        d = {}
        ans = []
        l = []
        for i in range(len(keyName)):
            l.append((keyName[i],count_time(keyTime[i])))
        l = sorted(l)
        name = \"\"
        a = []
        for item in l:
            k,v = item[0],item[1]
            if ans and k == ans[-1]:
                continue
            if k != name:
                a = [v]
                name = k
            else:
                if v - a[0] <= 60:
                    if len(a) == 2:
                        ans.append(k)
                        a = []
                        continue
                    a.append(v)
                else:
                    if len(a) == 1:
                        a = [v]
                    else:
                        if v - a[1] <= 60:
                            a = [a[1],v]
                        else:
                            a = [v]
        return ans
