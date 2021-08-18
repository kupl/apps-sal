class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        myDict = {}
        count = 0

        for i in range(0, len(time)):
            if (60 - time[i] % 60) % 60 in myDict:
                local = myDict.get((60 - time[i] % 60) % 60)
                count += len(local)

            local = []
            if time[i] % 60 in myDict:
                local = myDict.get(time[i] % 60)

            local.append(i)
            myDict[time[i] % 60] = local

        return count
