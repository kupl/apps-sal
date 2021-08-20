def main():
    n = int(input())
    ans = [0] * (2 * n)
    for i in range(n):
        a = 2 * i + 1
        b = 2 * i + 2
        if i & 1:
            ans[i] = a
            ans[i + n] = b
        else:
            ans[i] = b
            ans[i + n] = a
    ans *= 2
    curr = sum(ans[:n])
    mi = curr
    ma = curr
    for i in range(n, 4 * n):
        curr -= ans[i - n]
        curr += ans[i]
        mi = min(mi, curr)
        ma = max(ma, curr)
    if ma - mi > 1:
        print('NO')
    else:
        print('YES')
        print(*ans[:2 * n])
    return 0


main()
