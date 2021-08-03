from sys import stdin, stdout
for _ in range(1):  # int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    con0 = con1 = con2 = 0
    con1 = a[0]
    for i in range(1, n):
        con0, con1, con2 = max(con0, con1, con2), a[i] + con0, a[i] + con1
    print(max(con0, con1, con2))
