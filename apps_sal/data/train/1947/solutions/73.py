class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cover = [0] * 26
        for i in range(len(B)):
            cnt = [0] * 26
            for c in B[i]:
                cnt[ord(c) - ord('a')] += 1
            cover = [max(x, y) for x, y in zip(cover, cnt)]
        
        res = []
        for i in range(len(A)):
            cnt = [0] * 26
            for c in A[i]:
                cnt[ord(c) - ord('a')] += 1
            if all([x>=y for x, y in zip(cnt, cover)]):
                res.append(A[i])
        
        return res

