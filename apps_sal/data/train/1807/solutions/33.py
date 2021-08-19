class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        q = deque([])
        for i in range(2, n + 1):
            q.append((1, i))
        while q:
            (x, y) = q.popleft()
            if x == 1 or math.gcd(x, y) == 1:
                ans.append(f'{x}/{y}')
            if x + 1 < y:
                q.append((x + 1, y))
        return ans
