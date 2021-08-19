class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        Info = [[keyTime[i], keyName[i]] for i in range(len(keyName))]
        Info.sort()
        keyTime = [x[0] for x in Info]
        keyName = [x[1] for x in Info]
        cnt = collections.defaultdict(lambda: collections.deque())

        def diff(prev, curr):
            val = (int(curr[:2]) - int(prev[:2])) * 60 + int(curr[3:]) - int(prev[3:])
            return val > 60 or val < 0
        res = set()
        for i in range(len(keyName)):
            curr = keyTime[i]
            while cnt[keyName[i]] and diff(cnt[keyName[i]][0], curr):
                cnt[keyName[i]].popleft()
            if len(cnt[keyName[i]]) >= 2:
                res.add(keyName[i])
            cnt[keyName[i]].append(curr)
        return sorted(res)
