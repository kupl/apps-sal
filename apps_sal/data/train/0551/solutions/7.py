T = int(input())
while T > 0:
    s = input()
    flg = 0
    for i in range(len(s) - 1):
        if s.find(s[i], i + 1) != -1:
            flg = 1
    if flg == 0:
        print('no')
    else:
        print('yes')
    T = T - 1
