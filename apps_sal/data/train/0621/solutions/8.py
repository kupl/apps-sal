t = int(input())
while t > 0:
    n = int(input())
    s = input()
    words = s.split()
    substrings = []
    for i in words:
        tmp = []
        for j in range(len(i)):
            for k in range(j + 1, len(i) + 1):
                tmp.append(i[j:k])
        substrings.append(tmp)
    stem = ''
    for i in substrings[0]:
        flag = True
        for j in words:
            if i not in j:
                flag = False
        if flag == True and len(i) > len(stem):
            stem = i
        elif flag == True and len(i) == len(stem) and (i < stem):
            stem = i
    print(stem)
    t = t - 1
