class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        from collections import defaultdict
        name_time = defaultdict(list)
        access_violations = set()
        for n, t in zip(keyName, keyTime):
            name_time[n].append(t)

        for k, v in list(name_time.items()):
            if len(v) < 2:
                continue
            v.sort()
            if self.checkViolation(v):
                access_violations.add(k)

        access_violations = list(access_violations)
        access_violations.sort()
        return access_violations

    def checkViolation(self, access_times):
        from collections import deque
        access_time = deque()
        for t in access_times:
            access_time.append(t)
            if len(access_time) > 1:
                t_start = access_time[0]
                t_end = t

                if self.diff(t_start, t_end):
                    access_time.popleft()

                if len(access_time) >= 3:
                    return True

        return False

    def diff(self, t_start, t_end):
        h1, m1 = t_start.split(':')
        h2, m2 = t_end.split(':')

        if int(h2) - int(h1) >= 2:
            return True

        if int(h2) - int(h1) == 0:
            return False

        minutes = 60 - int(m1) + int(m2)

        if minutes <= 60:
            return False
        else:
            return True
