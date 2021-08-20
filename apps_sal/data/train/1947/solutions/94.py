class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        (ans, char_count, size_t) = (list(), Counter(), len(A))
        (T_A, T_B) = ([Counter(a) for a in A], [Counter(b) for b in B])
        for k in T_B:
            for c in k:
                if k[c] > char_count[c]:
                    char_count[c] = k[c]
        for i in range(len(T_A)):
            if not char_count - T_A[i] == {}:
                continue
            ans.append(A[i])
        return ans
