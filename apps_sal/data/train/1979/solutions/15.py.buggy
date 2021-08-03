class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def isValid(time):
            return (10 * time[0] + time[1] < 24) and (10 * time[2] + time[3] < 60)
        def perms(items):
            res = []
            if items == []:
                return [[]]
            for i in range(len(items)):
                #print(items, i, items[:i] + items[i+1::])
                res = res + [[items[i]] + rest_of_perm for rest_of_perm in perms(items[:i] + items[i+1::])]
            return res
        #print(perms(arr))
        validTimes = [t for t in perms(arr) if isValid(t)]
        if validTimes == []:
            return \"\"
        maxTime = max(validTimes)
        #print(maxTime)
        res = \"\".join([str(x) for x in maxTime])
        return res[:2] + \":\" + res[2::]
