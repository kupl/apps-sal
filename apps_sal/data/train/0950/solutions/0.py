N = int(input())
i = N + 1
flag = 0
for i in range(N + 1, 987654321):
    a = str(i)
    b = list(a)
    c = set(a)
    if '0' not in b:
        if len(b) == len(c):
            print(i)
            flag += 1
            break
if flag < 1:
    print(0)
