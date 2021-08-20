for _ in range(int(input())):
    (n, q) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (even, odd) = (0, 0)
    for j in range(n):
        count = bin(a[j]).count('1')
        if count % 2 == 0:
            even += 1
        else:
            odd += 1
    for j in range(q):
        m = int(input())
        temp = bin(m).count('1')
        (temp1, temp2) = (even, odd)
        if temp % 2 == 0:
            (temp1, temp2) = (even, odd)
        else:
            (temp1, temp2) = (odd, even)
        print(temp1, temp2)
