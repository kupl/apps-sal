class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0
        A.sort()
        avails = deque()
        for i in range(1, n):
            if A[i] > A[i - 1] + 1:
                avails.append([A[i - 1] + 1, A[i]])
            if i == n - 1:
                avails.append([A[i] + 1, A[i] + 2])
        (l, r) = avails.popleft()
        nexts = deque(range(l, r))
        r = nexts.popleft()
        pre = A[0]
        res = 0
        for i in range(1, n):
            if A[i] == pre:
                while r <= A[i]:
                    if nexts:
                        r = nexts.popleft()
                    elif avails:
                        (l, r) = avails.popleft()
                        nexts = deque(range(l, r))
                        r = nexts.popleft()
                    else:
                        r += 1
                res += r - A[i]
                A[i] = r
                if nexts:
                    r = nexts.popleft()
                elif avails:
                    (l, r) = avails.popleft()
                    nexts = deque(range(l, r))
                    r = nexts.popleft()
                else:
                    r += 1
            else:
                pre = A[i]
        return res
