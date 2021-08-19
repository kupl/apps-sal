c = 1
for test in range(int(input())):
    n = int(input())
    ans = pow(2, n, 8589934592) - 1
    ans = ans % 8589934592
    str1 = 'Case ' + str(c) + ': ' + str(ans)
    print(str1)
    c = c + 1
