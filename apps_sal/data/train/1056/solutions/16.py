# cook your dish here
for _ in range(int(input())):
    z = list(map(int, input().split()))
    if sum(z) == 180:
        print("YES")
    else:
        print("NO")
