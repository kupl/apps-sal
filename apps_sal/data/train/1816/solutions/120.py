from collections import deque


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dct = {i: [] for i in set(keyName)}
        for (i, j) in zip(keyName, keyTime):
            j = j.split(':')
            j = int(j[0]) * 60 + int(j[1])
            dct[i].append(j)
        print(dct)

        def check(arr):
            arr = sorted(arr)
            q = deque([arr[0]])
            for i in arr[1:]:
                while q:
                    if i > q[0] + 60:
                        q.popleft()
                    else:
                        break
                q.append(i)
                if len(q) >= 3:
                    return True
            return False
        res = [i for (i, j) in list(dct.items()) if check(j.copy())]
        res.sort()
        return res
