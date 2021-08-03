class Solution:
    def countLargestGroup(self, n: int) -> int:
        def countDigits(m):
            res = 0
            while m > 0:
                res += m % 10
                m //= 10
            return res
        dic = collections.defaultdict(list)
        for i in range(1, n + 1):
            count_i = countDigits(i)
            dic[count_i].append(i)

        max_count = max(len(dic[k]) for k in dic)
        res = [len(dic[k]) == max_count for k in dic]
        return sum(res)
