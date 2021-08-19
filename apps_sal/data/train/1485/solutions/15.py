# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    mini = 10000000
    count1, count2 = 0, 0
    u = []
    save = []
    for i in range(N):
        a = input()
        u.append(a)
        x = a[:N // 2].count('1')
        y = a[N // 2:].count('1')
        count1 += x
        count2 += y
        save.append(x - y)
    if(count1 == count2):
        print(0)
        continue
    for i in save:
        mini = min(abs(count1 - 2 * i - count2), mini)
    print(mini)
