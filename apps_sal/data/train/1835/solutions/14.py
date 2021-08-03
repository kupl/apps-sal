class Solution:
    def numsSameConsecDiff(self, n, k):
        d = {}
        for i in range(10):
            temp = set()
            if i + k <= 9:
                temp.add(i + k)
            if i - k >= 0:
                temp.add(i - k)
            d[i] = list(temp)

        res = []
        for i in range(1, 10):
            for neighbor in d[i]:
                res.append([i, neighbor])

        if n > 2:
            n -= 2
            while n > 0:
                temp = []
                for sublist in res:
                    for neighbor in d[sublist[-1]]:
                        temp.append(sublist + [neighbor])
                n -= 1
                res = temp
        for i in range(len(res)):
            res[i] = int(''.join(str(ele) for ele in res[i]))

        return res
