# cook your dish here
T = int(input())
for i in range(T):
    a, b, c = list(map(int, input().split()))
    # p=int(input())
    if a + b + c == 180:
        print("YES")
    else:
        print("NO")
