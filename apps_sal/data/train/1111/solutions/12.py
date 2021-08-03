t = int(input())
for _ in range(t):
    num = int(input())
    l = list(map(int, input().split()))
    even = 0
    for i in l:
        if i % 2 == 0:
            even += 1
    odd = num - even
    print(odd * even)
