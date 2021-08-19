for i in range(int(input())):
    n = int(input())
    (s1, s2) = (input(), input())
    b = [[int(s1[i]), int(s2[i])] for i in range(n)][::-1]
    a = 1
    ans = 'YES'
    for i in b:
        if i[a] > 2:
            if i[a ^ 1] < 3:
                ans = 'NO'
            else:
                a ^= 1
    if a != 0:
        ans = 'NO'
    print(ans)
