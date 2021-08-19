from datetime import datetime


class Solution:

    def alertNames(self, N: List[str], T: List[str]) -> List[str]:
        res = defaultdict(list)
        for i in range(len(N)):
            res[N[i]].append(T[i])
        for i in res:
            res[i] = sorted(res[i])
        final = []
        for emp in res:
            if len(res[emp]) < 3:
                continue
            else:
                (i, j) = (0, 2)
                while j < len(res[emp]):
                    a = datetime.strptime(res[emp][i], '%H:%M')
                    b = datetime.strptime(res[emp][j], '%H:%M')
                    if (b - a).seconds <= 3600:
                        final.append(emp)
                        break
                    else:
                        i += 1
                        j += 1
        return sorted(final)
