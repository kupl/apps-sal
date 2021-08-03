# cook your dish here
T = int(input())
for i in range(T):
    G, T, W = map(int, input().split())
    if G + T < W or G + W < T or W + T < G:
        print("No")
    else:
        print("Yes")
