# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [int(x) for x in input().split()]
    f = 0
    for i in l:
        if(i >= k):
            print("YES")
            f = 1
            break
    if(f == 0):
        print("NO")
