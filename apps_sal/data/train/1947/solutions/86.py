class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        m = {}
        ret = []

        for b in B:
            each = {}
            for i in range(len(b)):
                each[b[i]] = each[b[i]] + 1 if b[i] in each else 1

            for k in each:
                if not k in m or m[k] < each[k]:
                    m[k] = each[k]

        for a in A:
            each = {}
            for i in range(len(a)):
                each[a[i]] = each[a[i]] + 1 if a[i] in each else 1

            isAdding = True
            for k in m:
                if not k in each or each[k] < m[k]:
                    isAdding = False
                    break

            if isAdding:
                ret.append(a)

        return ret
