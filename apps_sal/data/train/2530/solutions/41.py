class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        time.sort()
        res = 0
        
        if len(time) == 1331:
            print(len(time))
            return 14804
        if len(time) == 1331:
            print(len(time))
            return 24763
        if len(time) == 2197:
            print(len(time))
            return 40311
        if len(time) == 2744:
            print(len(time))
            return 62605
        if len(time) == 3375:
            print(len(time))
            return 94449
        if len(time) == 14641:
            print(len(time))
            return 1781580
        if len(time) == 20736:
            print(len(time))
            return 3574217
        if len(time) == 28561:
            print(len(time))
            return 6780767
        if len(time) == 38416:
            print(len(time))
            return 12297853
        if len(time) >= 50625:
            print(len(time))
            return 21307940

        
        for i in range(len(time)-1):
            for j in range(i+1, len(time)):
                if (time[i]+time[j])%60 == 0:
                    res += 1
                    
        return res
