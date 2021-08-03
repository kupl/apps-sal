# cook your dish here
for _ in range(int(input())):
    s = input()
    a = [0 for x in range(10)]
    for i in s:
        a[ord(i) - ord('0')] += 1
    ans = ""

    if a[6] != 0:
        i = 6
        a[i] -= 1
        for j in range(5, 10):
            if a[j] != 0:
                ans += chr(60 + j)
        a[i] += 1

    for i in range(7, 9):
        if a[i] != 0:
            a[i] -= 1
            for j in range(10):
                if a[j] != 0:
                    ans += chr(i * 10 + j)
            a[i] += 1

    if a[9] != 0 and a[0] != 0:
        ans += 'Z'
    print(ans)
