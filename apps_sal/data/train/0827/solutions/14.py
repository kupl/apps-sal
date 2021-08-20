def get_ans(n, k, s):
    totalB = s.count('b')
    initialB = totalB * k
    ans = 0
    for i in s:
        if i == 'b':
            initialB -= 1
        elif i == 'a':
            APa = initialB
            APd = -totalB
            APn = k
            ans += APn * (2 * APa + (APn - 1) * APd) // 2
    return ans


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = input()
    print(get_ans(n, k, s))
