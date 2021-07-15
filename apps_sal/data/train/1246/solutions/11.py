# cook your dish here

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) == max(y):
        print("NO")
    else:
        print("YES")

