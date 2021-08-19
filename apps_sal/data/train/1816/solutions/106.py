from collections import defaultdict


def is_within_hour(time_1, time_2):
    [h_1, m_1] = time_1.split(':')
    [h_2, m_2] = time_2.split(':')
    if h_2 == h_1:
        return True
    if int(h_2) == int(h_1) + 1 and m_2 <= m_1:
        return True
    return False


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        logs = defaultdict(list)
        for (name, time) in zip(keyName, keyTime):
            logs[name].append(time)
        output = set()
        for name in logs:
            times = sorted(logs[name])
            for i in range(len(times) - 2):
                if is_within_hour(times[i], times[i + 2]):
                    output.add(name)
        return sorted(list(output))
