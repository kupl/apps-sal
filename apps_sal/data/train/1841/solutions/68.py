class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        x = sorted(arr)
        l = len(arr)

        median = x[(l - 1) // 2]
        # print(x, median)
        jj = sorted(list(range(len(arr))), key=lambda y: (abs(arr[y] - median), arr[y]), reverse=True)
        # print(jj)
        # print([(abs(arr[x]-median), x) for x in jj])
        n = [arr[i] for i in jj]
        # print(n)
        return n[:k]
