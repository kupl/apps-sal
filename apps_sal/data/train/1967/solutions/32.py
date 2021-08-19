class Solution:
    def ok(self, S, j, res):
        # print(j, res)
        if j == len(S):
            return True
        for k in range(j + 1, len(S) + 1):
            third = S[j:k]
            if len(third) > 1 and third[0] == '0' or int(third) >= 2 ** 31:
                continue
            third = int(third)
            if third == res[-1] + res[-2]:
                res.append(third)
                if self.ok(S, k, res):
                    return True
                else:
                    res.pop()
        return False

    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        res = []
        for i in range(1, n - 1):
            first = S[0:i]
            if len(first) > 1 and first[0] == '0' or int(first) >= 2 ** 31:
                continue
            for j in range(i + 1, n):
                second = S[i:j]
                if len(second) > 1 and second[0] == '0' or int(second) >= 2 ** 31:
                    continue
                res = [int(first), int(second)]
                if self.ok(S, j, res):
                    return res
                else:
                    res = []
        return res
