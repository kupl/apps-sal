import re
def bird_code(s):
    li = []
    for i in s:
        i = re.sub(r" *-", " ", i).upper().split()
        if len(i) == 1 : li.append(i[0][:4])
        if len(i) == 2 : li.append(i[0][:2] + i[1][:2])
        if len(i) == 3 : li.append(i[0][0] + i[1][0] + i[2][:2])
        if len(i) == 4 : li.append("".join([k[0] for k in i]))
    return li
