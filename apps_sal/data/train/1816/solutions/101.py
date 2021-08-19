class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        n = len(keyName)
        ans = set()

        def diffTime(h1, h2):
            h = int(h2[:2]) - int(h1[:2])
            m = int(h2[3:]) - int(h1[3:])
            if h >= 2 or h < 0:
                return False
            if h == 1:
                if m <= 0:
                    return True
                else:
                    return False
            return True
        arr = sorted(zip(keyTime, keyName))
        for i in range(n):
            keyName[i] = arr[i][1]
            keyTime[i] = arr[i][0]
        for i in range(n):
            if keyName[i] in ans:
                continue
            count = 1
            for j in range(len(d[keyName[i]]) - 1, -1, -1):
                if diffTime(d[keyName[i]][j], keyTime[i]):
                    count += 1
                    if count == 3:
                        ans.add(keyName[i])
                        break
            d[keyName[i]].append(keyTime[i])
        print(d)
        ans = sorted(ans)
        return ans
