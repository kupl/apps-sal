class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mycount = 0
        mydict = {k: [0, 0] for k in range(1, 30)}
        print(mydict)
        count0 = 0
        count30 = 0
        for tm in time:
            rest = tm % 60
            if rest == 0:
                count0 += 1
            elif rest == 30:
                count30 += 1
            elif rest > 30:
                mydict[60 - rest][1] += 1
            else:
                print(rest)
                mydict[rest][0] += 1
        for a in mydict:
            mycount += mydict[a][0] * mydict[a][1]
            # print(mycount)

        return mycount + (count30 - 1) * count30 // 2 + (count0 - 1) * count0 // 2
