T = int(input())
while(T > 0):
    [N, D] = list(map(int, input('').split()))
    carry = 0
    cal = 0
    ans = ''
    i = 1
    k = 0
    while i <= N:
        ans += str(chr(((carry + i) % 10) + ord('0')))
        carry = int((carry + i) / 10)
        cal += 1
        i += 1
        k += 1
    i -= 2
    while i >= 1:
        ans += str(chr(((carry + i) % 10) + ord('0')))
        carry = int((carry + i) / 10)
        cal += 1
        i -= 1
        k += 1
    while carry > 0:
        ans += str((((carry + i) % 10) + ord('0')))
        carry = int((carry) / 10)
        cal += 1
        k += 1
    ans = int(ans)
    ans *= (D * D)
    ans = str(ans)

    length = len(ans)
    ans1 = 0
    p = 1
    for i in range(length):
        ans1 = ((ord(ans[i]) - ord('0')) * p + ans1) % 1000000007
        p = (p * 23) % 1000000007
    print(ans1)

    T -= 1
