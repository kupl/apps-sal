class Solution:
    def longestAwesome(self, s: str) -> int:

        targets = {1 << x for x in range(10)}
        targets.add(0)

        print(targets)
        diction = {}
        res = 0
        prev = 0
        diction[0] = -1
        for idx, char in enumerate(s):
            curr = prev ^ 1 << int(char)
            if curr not in diction:
                diction[curr] = idx

            for target in targets:
                if curr ^ target in diction:
                    res = max(res, idx - diction[curr ^ target])

            prev = curr
        print(diction)
        print(res)
        return res
