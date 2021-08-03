class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def get_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        def is_alert(times):
            lent = len(times)
            if lent < 3:
                return False

            l, r = 0, 0
            for r in range(lent):
                if r - l >= 2 and times[r] - times[l] <= 60:
                    return True
                while l < r and times[r] - times[l] > 60:
                    l += 1
            return False

        lookup = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            lookup[name].append(get_minutes(time))

        alert_list = [name for name, times in lookup.items() if is_alert(sorted(times))]

        return sorted(alert_list)
