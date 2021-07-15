class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A: return 0
        repeat = collections.deque()
        A = sorted(A)
        for i,v in enumerate(A):
            if i and v == A[i-1]:
                repeat.append(v)
        slots = sorted(list(set(list(range(A[0],A[-1] + 1))) - set(A)))
        res = 0
        for i in slots:
            if repeat and i > repeat[0]:
                res += i - repeat[0]
                repeat.popleft()
        return res - sum(repeat) + sum([i for i in range(A[-1]+1,A[-1]+1+len(repeat))])
