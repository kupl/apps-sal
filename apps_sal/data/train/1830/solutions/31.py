# rains: 每个数代表一场雨，第i场雨下在rains[i]的这个lake上
# res: -1表示下雨，不能排水。res[i]表示要排干的那个lake
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # brute force
        lakesFull = {}
        n = len(rains)
        dry = []
        res = []        
        for i in range(n):
            #print (\"res:\" + str(res))
            #print(\"dry:\" + str(dry))
            #print(\"lakesFull:\" + str(lakesFull))
            l = rains[i]
            if l == 0:
                dry.append(i)
                res.append(-10000000)
                continue
            else:
                if l in lakesFull:
                    if len(dry) > 0:
                        di = -1
                        for dd in range(len(dry)):
                            if dry[dd] > lakesFull[l]:
                                di = dry[dd]
                                dry.pop(dd)
                                break
                        #if i == 10: print(\"di\" + str(di))
                        if di >= 0:
                            res[di] = l
                            del lakesFull[l]
                        else: 
                            return []
                    else:
                        return []
                lakesFull[l] = i
                res.append(-1)
        #print (res)
        #print (dry)
        #print (lakesFull)
        for i in range(n):
            if res[i] == -10000000: res[i] = 1
        return res
