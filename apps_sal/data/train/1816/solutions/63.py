class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        result = []
        tracker = {}
        for (person, time) in zip(keyName, keyTime):
            try:
                if tracker[person] and person not in result:
                    tracker[person].append(time)
                    tracker[person].sort()
                    if len(tracker[person]) >= 3:
                        for i in range(1, len(tracker[person]) - 1):
                            lh = tracker[person][i - 1].split(':')[0]
                            ch = tracker[person][i].split(':')[0]
                            rh = tracker[person][i + 1].split(':')[0]
                            tocheck = [lh, ch, rh]
                            if int(lh) <= int(ch) and int(ch) <= int(rh):
                                if '23' in tocheck and '00' in tocheck:
                                    break
                                l = int(lh + tracker[person][i - 1].split(':')[1])
                                c = int(ch + tracker[person][i].split(':')[1])
                                r = int(rh + tracker[person][i + 1].split(':')[1])
                                diff = c - l + (r - c)
                                if diff <= 100:
                                    result.append(person)
                                    break
            except:
                tracker[person] = [time]
        return sorted(result)
