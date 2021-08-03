for i in range(int(input())):
    ans = 0
    str1 = input()
    n = len(str1)
    for j in range(n - 1):
        if str1[j] == str1[j + 1]:
            ans += ((n * (n - 1)) // 2)
        else:
            ans += n
    print(ans)
