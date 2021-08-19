'''


1
10
5 15 1 66 55 32 40 22 34 11
38

Step 1: 15 5 66 1 32 55 22 40 11 34

Step 2: 15 7 66 2 34 56 23 41 13 35

Step 3: 35 13 41 23 56 34 2 66 7 15

35 is the number lesser than 38 and 41 is the number greater than 38 in the given set of numbers.

'''


n = int(input())
for i in range(0, n):
    o = int(input())
    p = input().rstrip().split(' ')
    x = int(input())
    for j in range(0, len(p) - 1, 2):
        A = int(p[j])
        B = int(p[j + 1])
        p[j] = B + (B % 3)
        p[j + 1] = A + (A % 3)
    if len(p) % 2 == 1:
        p[len(p) - 1] = int(p[len(p) - 1]) + (int(p[len(p) - 1])) % 3
    # print(p)
    p.sort(key=int)
    ans1 = -1
    ans2 = -1
    I = 0
    J = len(p) - 1
    while(I <= J):
        m = (I + J) // 2
        if int(p[m]) >= x:
            J = m - 1
        else:
            ans1 = int(p[m])
            I = m + 1
    I = 0
    J = len(p) - 1
    while(I <= J):
        m = (I + J) // 2
        if int(p[m]) <= x:
            I = m + 1
        else:
            ans2 = int(p[m])
            J = m - 1
    print(ans1, ans2)
