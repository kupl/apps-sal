class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) // 2
        A_map = defaultdict(int)
        for a in A:
            A_map[a] += 1
            if A_map[a] == N:
                return a
