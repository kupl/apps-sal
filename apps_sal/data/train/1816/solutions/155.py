from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        workers = defaultdict(list)
        tup = [[keyTime[i], keyName[i]] for i in range(len(keyTime))]
        for i in range(len(keyName)):
            workers[tup[i][1]].append(tup[i][0])
        answer = []
        for worker, times in list(workers.items()):
            i, j = 0, 0
            stimes = sorted(times)

            while j < len(stimes):
                hh1 = int(stimes[i][:2])
                hh2 = int(stimes[j][:2])
                mm1 = int(stimes[i][3:])
                mm2 = int(stimes[j][3:])

                if hh1 == hh2 or (abs(hh1 - hh2) == 1 and mm2 + (60 - mm1) <= 60):
                    if j - i + 1 == 3:
                        answer.append(worker)
                        break
                    j += 1
                else:
                    i += 1
        return sorted(answer)
