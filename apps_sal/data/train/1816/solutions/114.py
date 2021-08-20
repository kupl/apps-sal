class Solution:

    def alertNames(self, keyName, keyTime):
        name_to_time = collections.defaultdict(list)
        for (name, hour_minute) in zip(keyName, keyTime):
            (hour, minute) = map(int, hour_minute.split(':'))
            time = hour * 60 + minute
            name_to_time[name].append(time)
        names = []
        for (name, time_list) in name_to_time.items():
            time_list.sort()
            q = collections.deque()
            for t in time_list:
                q.append(t)
                while q[0] < t - 60:
                    q.popleft()
                if len(q) > 2:
                    names.append(name)
                    break
        return sorted(names)
