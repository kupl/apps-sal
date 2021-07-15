for _ in range(int(input())):
    d = dict()
    count = 0
    for i in range(int(input())):
        ip = input().split()
        if ip[0] in d:
            if int(ip[1]) == 1:
                d[ip[0]][1] += 1
            else:
                d[ip[0]][0] += 1
        else:
            if int(ip[1]) == 1:
                d.update({
                    ip[0]: {0: 0, 1: 1}
                })
            else:
                d.update({
                    ip[0]: {0: 1, 1: 0}
                })
    for j in d.values():
        count += max(j.values())
    print(count)
