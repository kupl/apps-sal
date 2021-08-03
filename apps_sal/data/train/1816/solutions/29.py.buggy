class Solution:
    def lastOneHour(self, end, cur):
        endHr = end.split(\":\")
        curHr = cur.split(\":\")
        if int(endHr[0]) - int(curHr[0]) == 0:
            return True
        if int(endHr[0]) - int(curHr[0]) == 1 and ((int(endHr[1]) + 60 - int(curHr[1])) <= 60):
            return True
        return False
    
    def checkHour(self, l):
        if len(l) <= 2:
            return False
        i = 0
        j = 1
        while j < len(l):
            if self.lastOneHour(l[j], l[i]):
                j+=1
                if j - i >= 3:
                    return True
            else:
                i+=1
        return False
        
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        res = []
        for i in range(0, len(keyName)):
            # print(\"\
######\")
            name = keyName[i]
            # print(f\"Name: {name} Time: {keyTime[i]}\")
            if name not in d:
                # print(f\"Name not in d. Adding: {d}\")
                d[name] = [[keyTime[i]], False]
            else:
                # print(\"Name is in d\")
                # print(d[name])
                if not d[name][1]:
                    d[name][0].append(keyTime[i])
                    d[name][0].sort()
                    cur = 0
                    if self.checkHour(d[name][0]):
                        res.append(name)
                        d[name][1] = True
                    
#                     while cur < len(d[name][0]):
#                         r = self.lastOneHour(d[name][0][-1], d[name][0][cur])
#                         if not r:
#                             cur+=1
#                         else:
#                             break
#                     if len(d[name][0]) - cur >= 3:
                        # res.append(name)
                        # d[name][1] = True
                # print(d[name])
        res.sort()
        return res
