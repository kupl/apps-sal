class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A, B, n = [], [], len(costs) // 2
        diff = []
        for i, (a, b) in enumerate(costs):
            diff.append((i, (a - b)))
            if a < b:
                A.append(i)
            else:
                B.append(i)

        flag = 0
        if len(A) > len(B):
            flag = 1
            diff = sorted(diff, key=lambda x: x[1], reverse=True)
            for i, x in diff:
                if x > 0 or i in B:
                    continue
                B.append(i)
                if len(B) == n:
                    break

        elif len(A) < len(B):
            flag = 2
            diff = sorted(diff, key=lambda x: x[1])

            for i, x in diff:
                if i in A:
                    continue
                A.append(i)
                if len(A) == n:
                    break

        res = 0
        for i in range(2 * n):
            a, b = costs[i]
            if flag == 1:
                res += b if i in B else a

            if flag == 2 or flag == 0:
                res += a if i in A else b

        return res
