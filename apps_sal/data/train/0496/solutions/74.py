class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        diff = 0
        stack = []
        c = Counter(A)
        for i in range(min(c.keys()), max(c.keys()) + 1):
            if i in c:
                stack += [i] * (c[i] - 1)
            elif i not in c and stack:
                diff += i - stack.pop()
        return diff + sum(range(i + 1, i + 1 + len(stack))) - sum(stack)
