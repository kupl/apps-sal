# cook your dish here
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    c = 1
    for i in arr:
        c = c * i
    if c % 2 != 0:
        print("YES")
    else:
        print("NO")
