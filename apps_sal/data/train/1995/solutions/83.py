class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passIn = [[item[1], item[0]] for item in trips]
        passOut = [[item[2], -item[0]] for item in trips]
        setOfTimes = list(set([item[1] for item in trips] + [item[2] for item in trips]))
        setOfTimes.sort()
        ans = True
        counter = 0
        for time in setOfTimes:
            if ans == True:
                for item in passIn + passOut:
                    if item[0] == time:
                        counter += item[1]
                if counter > capacity:
                    ans = False
        return ans
