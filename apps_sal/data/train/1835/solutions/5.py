class Solution:
    def numsSameConsecDiff(self, n, k):
        res = []
        for i in range(1, 10):
            neighbors = self.helper(i, k)
            for neighbor in neighbors:
                res.append([i, neighbor])

        if n > 2:
            n -= 2
            while n > 0:
                temp = []
                for sublist in res:
                    neighbors = self.helper(sublist[-1], k)
                    for neighbor in neighbors:
                        temp.append(sublist + [neighbor])
                n -= 1
                res = temp
        for i in range(len(res)):
            res[i] = int(''.join(str(ele) for ele in res[i]))

        return res

    def helper(self, val, k):
        res = set()
        if val + k <= 9:
            res.add(val + k)
        if val - k >= 0:
            res.add(val - k)
        return res
