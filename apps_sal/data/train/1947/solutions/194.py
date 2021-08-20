class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        a_counts = [Counter(a) for a in A]
        b_count = Counter()
        for b in B:
            for (l, c) in list(Counter(b).items()):
                b_count[l] = max(b_count[l], c)
        uni = []
        for (i, ac) in enumerate(a_counts):
            is_universal = True
            for (l, c) in list(b_count.items()):
                if ac[l] < c:
                    is_universal = False
                    break
            if is_universal:
                uni.append(A[i])
        return uni
