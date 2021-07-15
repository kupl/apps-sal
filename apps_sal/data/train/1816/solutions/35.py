import time
class Solution:
    def alertNames(self, keyName, keyTime) :
        hmap = {}
        for i in range(len(keyName)):
            if keyName[i] in hmap:
                hmap[keyName[i]].append(keyTime[i])
            else:
                hmap[keyName[i]] = [keyTime[i]]
        tempKeyName,tempKeyTime = list(keyName),list(keyTime)
        keyName = []
        temp = []
        for k,v in hmap.items():
            tempV = []
            for i in v:
                t = i.split(\":\")
                tempV.append(int(t[0])*60 + int(t[-1]))
            tempV.sort()
            for j in tempV:
                keyName.append(k)
                temp.append(j)

            

        # temp = []
        # for i in keyTime:
        #     t = i.split(\":\")
        #     temp.append(int(t[0])*60 + int(t[-1]))
        # keyTime = [int(\"\".join(list(str(i).split(\":\")))) for i in keyTime]
        # print(temp)
        res,i,currCount,currName,startTime,endtime = [],1,1,keyName[0],temp[0],temp[0]+60
        while i < len(keyName):
            t = i
            while i < len(keyName) and keyName[i] == keyName[i-1] and temp[i] <= endtime and temp[i] > startTime:
            # keyTime[i] > keyTime[i-1] and :
                currCount += 1
                i += 1
            if i >= len(keyName):
                break
            if currCount >= 3:
                res.append(currName)
                currCount = 0
                currName = keyName[i]
                startTime = temp[i]
                endtime = startTime + 60
            else:
                currCount = 1
                i = t+1
                currName = keyName[t]
                startTime = temp[t]
                endtime = startTime + 60
        if currCount >=3 :
            res.append(currName)
        res = list(set(res))
        res.sort()
        return res

# s = Solution()
# keyName =[\"a\",\"a\",\"a\",\"a\",\"a\",\"a\",\"b\",\"b\",\"b\",\"b\",\"b\"]; keyTime =[\"23:27\",\"03:14\",\"12:57\",\"13:35\",\"13:18\",\"21:58\",\"22:39\",\"10:49\",\"19:37\",\"14:14\",\"10:41\"]
# print(s.alertNames(keyName,keyTime))

