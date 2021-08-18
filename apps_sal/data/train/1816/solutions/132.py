class Worker(object):
    def __init__(self, name):
        self.name = name
        self.minutes = []

    def add(self, time):
        h, m = tuple(time.split(':'))
        h, m = int(h), int(m)
        self.minutes.append(h * 60 + m)

    def is_alert(self):
        self.minutes.sort()
        for i, lower in enumerate(self.minutes):
            upper = lower + 60
            j = bisect.bisect_right(self.minutes, upper)
            if j - i >= 3:
                return True
        return False


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        workers = {}
        for name, time in zip(keyName, keyTime):
            if name not in workers:
                workers[name] = Worker(name)
            workers[name].add(time)

        ans = []
        for name, worker in workers.items():
            if worker.is_alert():
                ans.append(name)
        return sorted(ans)
