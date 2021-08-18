class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def oneHourAgo(time1, time2):
            hr_min1 = time1.split(':')
            hr_min2 = time2.split(':')

            if abs(int(hr_min2[0]) - int(hr_min1[0])) > 1 or (abs(int(hr_min2[0]) - int(hr_min1[0])) == 1 and int(hr_min1[1]) < int(hr_min2[1])):
                return True
            else:
                return False
        result = set()

        timeline = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            timeline[name].append(time)

        for name in keyName:
            timeline[name].sort()

        for name in keyName:
            q = deque()
            inside_q = 0
            for time in timeline[name]:
                while q and (oneHourAgo(q[0], time)):
                    q.popleft()
                    inside_q -= 1

                q.append(time)
                inside_q += 1

                if inside_q >= 3:
                    result.add(name)
                    break

        result = list(result)
        result.sort()
        return result
