t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            temp = s[:]
            for k in range(i, j + 1):
                if(temp[k] == '1'):
                    temp[k] = '0'
                else:
                    temp[k] = '1'
            for k in range(n - 1):
                if(temp[k] == temp[k + 1]):
                    cnt += 1
    print(cnt)
