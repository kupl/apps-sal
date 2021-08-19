# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split(" "))

    l = []
    for i in range(1, n + 1):
        l.append(i)

    l[-1], l[k] = l[k], l[-1]
    for i in l:
        print(i, end=" ")
