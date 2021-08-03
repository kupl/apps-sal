class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_to_time = collections.defaultdict(list)
        for name, hour_minute in zip(keyName, keyTime):
            hour, minute = list(map(int, hour_minute.split(':')))
            time = hour * 60 + minute
            name_to_time[name].append(time)
        names = []
        for name, time_list in list(name_to_time.items()):
            time_list.sort()
            dq = collections.deque()
            for time in time_list:
                dq.append(time)
                if dq[-1] - dq[0] > 60:
                    dq.popleft()
                if len(dq) >= 3:
                    names.append(name)
                    break
        return sorted(names)
