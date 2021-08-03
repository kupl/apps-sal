n = int(input())
li = []
for i in range(n):
    string, pri = input().split()
    pri = int(pri)
    li.append([string, pri])
li.sort(key=lambda x: x[1], reverse=True)
q = int(input())
for i in range(q):
    start = input()
    f = 0
    for i in range(n):
        if li[i][0].startswith(start):
            f = 1
            print(li[i][0])
            break
    if not f:
        print('NO')
