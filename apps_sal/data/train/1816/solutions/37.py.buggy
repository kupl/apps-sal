class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        newlist = [[keyName[i],int(keyTime[i].split(\":\")[0])*60+int(keyTime[i].split(\":\")[1])] for i in range(len(keyName))]
        newlist = sorted(newlist, key = lambda x: x[1])
        print(newlist)
        res = []
        last = collections.defaultdict(list)
        for i in range(len(keyName)):
            if newlist[i][0] in res:
                continue
            if newlist[i][0] not in last:
                last[newlist[i][0]].append(newlist[i][1])
            else:
                while len(last[newlist[i][0]])>0 and newlist[i][1] -last[newlist[i][0]][0]>60:
                    last[newlist[i][0]].pop(0)
                last[newlist[i][0]].append(newlist[i][1])
                if len(last[newlist[i][0]])>=3:
                    res.append(newlist[i][0])
        return sorted(res)
        # for i in range(len(keyName)):
        #     if keyName[i] in res:
        #         continue
        #     if keyName[i] not in last:
        #         curh =int(keyTime[i].split(\":\")[0])
        #         curmin = int(keyTime[i].split(\":\")[1])
        #         last[keyName[i]].append(curh*60+curmin)
        #     else:
        #         curh = int(keyTime[i].split(\":\")[0])
        #         curmin = int(keyTime[i].split(\":\")[1])
        #         curtime = curh*60+curmin
        #         # if curtime<last[keyName[i]][-1]:
        #         #     curtime+=24*60
        #         while len(last[keyName[i]])>0 and (curtime-last[keyName[i]][0]>60 or curtime-last[keyName[i]][0]<0):
        #             last[keyName[i]].pop(0)
        #         last[keyName[i]].append(curtime)
        #         if len(last[keyName[i]])>=3:
        #             res.append(keyName[i])
        # return sorted(res)
