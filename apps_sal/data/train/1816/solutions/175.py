from collections import deque

class TimeTracker:
    
    def __init__(self):
        self.users = defaultdict(deque)
        
    def add(self, name, time):
        self.users[name].append(time)
        while (self.users[name][-1] - self.users[name][0]) > 60:
            self.users[name].popleft()
        if len(self.users[name]) >= 3:
            return True
        return False

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        alerts = set()
        tracker = TimeTracker()
        names = sorted([(name, convert_time(time)) for name, time in zip(keyName, keyTime)])
        for name, time in names:
            if tracker.add(name, time):
                alerts.add(name)
        return sorted(alerts)
        
def convert_time(timestamp):
    hours, minutes = timestamp.split(':')
    time = int(hours) * 60 + int(minutes)
    return time
