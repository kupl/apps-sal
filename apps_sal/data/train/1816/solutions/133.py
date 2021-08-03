class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)

        keylist = list(zip(keyName, keyTime))
        keylist = sorted(keylist, key=lambda x: x[1])
        # print(keylist)
        ans = set()
        for name, t in keylist:

            #print(name, t)
            if len(d[name]) < 3:
                d[name].append(t)
            elif len(d[name]) == 3:
                d[name].pop(0)
                d[name].append(t)

            if len(d[name]) == 3:
                begin = d[name][0].split(':')
                end = d[name][2].split(':')
                #print(name, begin, end)
                if begin[0] == end[0]:
                    ans.add(name)
                elif int(begin[0]) + 1 == int(end[0]) and int(begin[1]) >= int(end[1]):
                    ans.add(name)
        # print(d)
        ans = list(ans)
        ans.sort()
        return ans
