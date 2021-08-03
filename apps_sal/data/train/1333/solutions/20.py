def get_num_of_ones(x):
    c = 0
    while (x):
        x &= x - 1
        c += 1
    return c


mod = 10 ** 9 + 7
twopow = {x: pow(2, x) % mod for x in range(35)}
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    ones_in_prev = 0
    ones_in_current = 0
    ans = 1
    flag = True
    ones_in_current = get_num_of_ones(b[0])
    ones_in_prev = ones_in_current
    for i in range(1, n):
        ans *= twopow[ones_in_prev]
        ans %= mod
        ones_in_current = get_num_of_ones(b[i])
        ones_in_prev = ones_in_current
        if (b[i] < b[i - 1]):
            flag = False
            break
    if(flag):
        print(ans % mod)
    else:
        print(0)
