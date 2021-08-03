def dtob(num):
    if num > 1:
        dtob(num // 2)
    return(num % 2)


t = int(input())
for _ in range(t):
    n = int(input())
    value = list(map(int, input().split()))
    l = []
    for i in range(len(value)):
        b = dtob(value[i])
        if(b % 10 == 0):
            l.append(value[i])
    print(sum(l))
