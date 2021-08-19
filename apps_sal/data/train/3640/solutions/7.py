def funnel_out(lst):
    ans = ''
    while lst != [[]]:
        temp = []
        for i in range(len(lst) - 1, -1, -1):
            x = lst[i]
            x2 = lst[i - 1]
            if i == len(lst) - 1:
                ans += x[0]
                if len(lst) == 1:
                    lst = [[]]
                    break
                lst[i] = [min([k for k in x2 if k != ''])] if len(lst) > 1 else []
                lst[i - 1][x2.index(min([k for k in x2 if k != '']))] = ''
            elif i == 0:
                if all((j == '' for j in lst[0])):
                    lst = lst[1:]
                else:
                    break
            else:
                for j in range(len(x)):
                    if x[j] == '':
                        (a, b) = (x2[j], x2[j + 1])
                        t = [k for k in (a, b) if k != '']
                        val = min(t) if t != [] else ''
                        idx = j if x2[j] == val else j + 1
                        x[j] = val
                        x2[idx] = ''
    return ans
