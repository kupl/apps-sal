t = int(input())
i = 0
while(i != t):
    lst = list(map(int, input().split()))
    B = lst[0]
    G = lst[1]
    result = max(B, G) * 2 + (min(B, G) - 1) * 2
    print(result)
    i += 1
