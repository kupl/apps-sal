def diff(time2, time1):
    t1 = int(time1[:2]) * 60 + int(time1[3:])
    t2 = int(time2[:2]) * 60 + int(time2[3:])
    return t2 - t1


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        l = []
        for (name, time) in zip(keyName, keyTime):
            l.append((name, time))
        l = sorted(l, key=lambda x: x[1])
        keyName = [i[0] for i in l]
        keyTime = [i[1] for i in l]
        result = set()
        index = 0
        hash_map = {}
        i = 0
        while i < len(keyName):
            name = keyName[i]
            time = keyTime[i]
            dif = diff(time, keyTime[index])
            if dif > 60 or dif < 0:
                if dif < 0:
                    index = i
                    hash_map.clear()
                    hash_map[name] = 1
                    i += 1
                    continue
                elif dif > 60:
                    hash_map[keyName[index]] -= 1
                    index += 1
                    continue
            if hash_map.get(name, -1) == -1:
                hash_map[name] = 1
            else:
                hash_map[name] += 1
            if hash_map[name] >= 3:
                result.add(name)
            i += 1
        result = sorted(list(result))
        return result
