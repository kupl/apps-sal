def within_hour(large, small):
    if abs(large[0] - small[0]) >= 2:
        return False
    if large[0] - small[0] == 1 and small[1] < large[1]:
        print((large, small))
        return False
    return True


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        sorted_list = sorted(zip(keyTime, keyName))
        alerted = []
        people = {}
        for time_str, name in sorted_list:
            if name not in alerted:
                time = [int(time_str[:2]), int(time_str[-2:])]
                if name in list(people.keys()):
                    if len(people[name]) == 2:
                        if within_hour(time, people[name][1]):
                            people[name].append(time)
                            if not within_hour(time, people[name][0]):
                                del people[name][0]
                            else:
                                alerted.append(name)
                        else:
                            people[name] = [time]
                    else:
                        if not within_hour(time, people[name][0]):
                            people[name] = [time]
                        else:
                            people[name].append(time)
                else:
                    people[name] = [time]
        return sorted(alerted)
