class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        arr1 = []
        arr2 = []
        for x in A:
            arr1.append(collections.Counter(x))
        dic = collections.defaultdict(int)
        for y in B:
            t = collections.Counter(y)
            for c in t:
                dic[c] = max(dic[c], t[c])
        res = []

        def comp(i):
            for c in dic:
                if arr1[i][c] < dic[c]:
                    return False
            return True

        for i in range(len(A)):
            if comp(i):
                res.append(A[i])
        return res
