def compareTimesStr(beginStr, endStr):
    return compareTimes(int(beginStr[:2]), int(beginStr[-2:]), int(endStr[:2]), int(endStr[-2:]))


def compareTimes(beginHr: int, beginMin: int, endHr: int, endMin: int):
    if endHr < beginHr:
        return False
    if beginHr == endHr:
        return True
    elif endHr - beginHr > 1:
        return False
    else:
        return endMin - beginMin <= 0


def hasAlert(times: List[str]) -> bool:
    if len(times) < 3:
        return False
    times.sort()
    i = 0
    while i < len(times) - 2:
        if compareTimesStr(times[i], times[i + 2]):
            return True
        i += 1
    return False


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = []
        if len(keyName) < 3:
            return ans
        zippedPairs = list(zip(keyName, keyTime))
        keyTime = [x for (_, x) in sorted(zippedPairs)]
        print(keyTime)
        keyName.sort()
        start = 0
        for i in range(len(keyName)):
            if keyName[i] == keyName[start] and i < len(keyName) - 1:
                pass
            elif i < len(keyName) - 1:
                if hasAlert(keyTime[start:i]):
                    ans.append(keyName[start])
                start = i
            elif hasAlert(keyTime[start:i + 1]):
                ans.append(keyName[start])
        return sorted(ans)
