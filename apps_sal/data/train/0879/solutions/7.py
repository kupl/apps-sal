summ = [0, 45, 40, 45, 40, 25, 40, 45, 40, 45, 0]
arr = []
for i in range(0, 10):
    curr = []
    for j in range(1, 11):
        mul = i * j
        rem = mul % 10
        curr.append(rem)
    arr.append(curr)
for _ in range(int(input())):
    (num, n) = (int(x) for x in input().split())
    count = num // (n * 10)
    ans = count * summ[n % 10]
    rem = (num - count * (n * 10)) // n
    c = 0
    for i in range(rem):
        s = n % 10
        c += arr[s][i]
    print(ans + c)
