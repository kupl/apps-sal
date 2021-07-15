class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        key_uses = list(sorted(zip(keyName, keyTime)))
        alerts = set()
        uses_by_user = collections.defaultdict(deque)
        for user, time in key_uses:
            hr, mn = time.split(':')
            tm = int(hr) * 60 + int(mn)
            uses_by_user[user].append(tm)
            print((uses_by_user[user][0]))
            while uses_by_user[user][0] < tm - 60:
                uses_by_user[user].popleft()
            if len(uses_by_user[user]) > 2:
                alerts.add(user)
        return sorted(list(alerts))

