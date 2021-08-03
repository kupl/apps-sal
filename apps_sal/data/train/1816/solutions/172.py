class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ar = sorted(zip(keyTime, keyName))
        d = dict()
        ans = set()
        n = len(ar)

        i, j = 0, 0

        while i < n:
            time, name = ar[i]
            hour, minute = map(int, time.split(':'))
            timeLimit = str(hour - 1).zfill(2) + ':' + str(minute).zfill(2)

            while j < i and ar[j][0] < timeLimit:
                d[ar[j][1]] -= 1
                j += 1

            d[name] = 1 + d.get(name, 0)
            if d[name] >= 3:
                ans.add(name)
            i += 1

        return sorted(ans)
