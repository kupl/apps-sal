Global_data = [(1, 0), (10, 45), (5, 20), (10, 45), (5, 20), (2, 5), (5, 20), (10, 45), (5, 20), (10, 45)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    kol = a // b
    last = b % 10
    ans = kol // Global_data[last][0] * Global_data[last][1]
    c = 0
    for i in range(kol % Global_data[last][0]):
        c += last
        c %= 10
        ans += c
    print(ans)
