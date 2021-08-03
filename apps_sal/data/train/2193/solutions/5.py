n = int(input())
x = []
for i in range(1, n + 1):
    l = list(map(int, input().split()))
    x.append([i, sum(l)])
x.sort(key=lambda x: x[1], reverse=True)
c = 0
for i in x:
    c += 1
    if(i[0] == 1):
        print(c)
        break
