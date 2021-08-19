t = int(input())
for _ in range(t):
    s = [x for x in input()]
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    flag = 0
    for (keys, values) in freq.items():
        if values >= 2:
            flag = 1
            break
    if flag == 0:
        print('no')
    else:
        print('yes')
