class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans, n, i, pool = [], len(keyName), 0, sorted([[name, time] for name, time in zip(keyName, keyTime)])
        while i < n:
            j, cur = i + 1, collections.deque()
            while j < n and pool[j][0] == pool[i][0]:
                j += 1
            for k in range(i, j):
                time = int(pool[k][1][:2]) * 60 + int(pool[k][1][3:])
                while cur and cur[0] < time - 60:
                    cur.popleft()
                if len(cur) > 1:
                    ans.append(pool[k][0])
                    break
                cur.append(time)
            i = j
        return ans
