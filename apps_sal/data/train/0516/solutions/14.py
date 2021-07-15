t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    sum = 0
    for i in range(1, n+1):
        c = num[i-1]
        count_for = 0
        count_bac = 0
        for j in range(i, n):
            if num[j] < c:
                count_for += 1
        for j in range(i):
            if num[j] < c:
                count_bac += 1
        count = count_for + count_bac
        p = (k*(k+1))//2 * count
        p = p - k * count_bac
        sum = sum + p
    print(sum)


