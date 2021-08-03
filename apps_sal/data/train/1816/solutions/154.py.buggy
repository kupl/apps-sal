def convert_time(str_time):
    return [int(segment) for segment in str_time.split(\":\")]


def within(next_time, last_time):
    # compute the next_time - last_time
    next_h = next_time[0]
    next_m = next_time[1]
    
    last_h = last_time[0]
    last_m = last_time[1]

        
    if next_h == last_h:
        return True
    elif next_h > last_h:
        # 10:07 - 09:08 = 607 - 548 = 59
        diff = next_h * 60 + next_m - (last_h * 60 + last_m)
        return diff <= 60
    else:
        # next_h < last_h
        # 00:01 - 23:59 = 24 * 60 + 1 - 23 * 60 + 59 = 1441 - 1439
        diff = (next_h + 24) * 60 + next_m - (last_h * 60 + last_m)
        return diff <= 60

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_to_time = {}
        
        # daniel => [10:00, 10:40, ...]
        # luis => [....]
        for name, time in zip(keyName, keyTime):
            if name in name_to_time:
                name_to_time[name].append(convert_time(time))
            else:
                name_to_time[name] = [convert_time(time)]
        
        for name in name_to_time:
            name_to_time[name].sort(key=lambda time: (time[0], time[1]))
        
        alerted = []
        window = 3
        for name in name_to_time:
            for i in range(len(name_to_time[name]) - window + 1):
                current_time = name_to_time[name][i]
                count = 1
                for j in range(1, window):
                    next_time = name_to_time[name][i + j]
                    if within(next_time, current_time):
                        count += 1
                    
                if count == 3:
                    alerted.append(name)
                    break
                    
            # count = 1
            # last_time = name_to_time[name][0]
            # for i in range(1, len(name_to_time[name])):
            #     next_time = name_to_time[name][i]
            #     inside = within(next_time, last_time)
            #     if inside:
            #         count += 1
            #     else:
            #         count = 1
            #     last_time = next_time
            #     if count >= 3:
            #         alerted.append(name)
            #         break
        
        alerted.sort()
        return alerted
        
        
