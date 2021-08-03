
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_to_time = collections.defaultdict(list)
        for name, hour_minute in zip(keyName, keyTime):
            hour, minute = map(int, hour_minute.split(':'))
            time = hour * 60 + minute
            name_to_time[name].append(time)
        names = []
        for name, time_list in name_to_time.items():
            time_list.sort()
            for i, time in enumerate(time_list):
                if i >= 2 and time - time_list[i - 2] <= 60:
                    names.append(name)
                    break
        return sorted(names)
