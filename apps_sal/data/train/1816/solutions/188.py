from collections import Counter


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def _convertTime(x):
            h = int(x[0:2])
            m = int(x[3:5])
            t = h * 60 + m
            return t
        keyTime = [_convertTime(el) for el in keyTime]
        keys = list(zip(keyTime, keyName))
        keys = sorted(keys)
        people = {}
        for key in keys:
            if key[1] in people:
                people[key[1]].append(key)
            else:
                people[key[1]] = [key]
        ans = []
        for (person, keys) in list(people.items()):
            q = []
            for key in keys:
                time = key[0]
                q.append(time)
                while q[0] + 60 < q[-1]:
                    q.pop(0)
                if len(q) >= 3:
                    ans.append(key[1])
                    break
        return sorted(ans)
