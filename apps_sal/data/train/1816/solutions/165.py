class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        record = {}

        def to_mininute(time):
            h, m = [int(t) for t in time.split(':')]
            return h * 60 + m
        keyTime = list(map(to_mininute, keyTime))
        data = list(zip(keyTime, keyName))
        data.sort()
        for time, name in data:
            if name not in record:
                record[name] = []
            record[name].append(time)
        ans = set()
        for name, times in list(record.items()):
            print((name, times))
            l = len(times)
            for i in range(2, l):
                #print(times[i], times[i - 2])
                if times[i] - times[i - 2] <= 60:
                    ans.add(name)
                    break
            # print(sorted(list(ans)))
        return sorted(list(ans))
