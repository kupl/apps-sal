from sys import stdin, stdout
t = int(input())
for i in range(t):
    (n, q) = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    (even, odd) = (0, 0)
    for j in range(n):
        count = bin(a[j]).count('1')
        if count % 2 == 0:
            even += 1
        else:
            odd += 1
    for j in range(q):
        m = int(stdin.readline())
        temp = bin(m).count('1')
        (temp1, temp2) = (even, odd)
        if temp % 2 == 0:
            (temp1, temp2) = (even, odd)
        else:
            (temp1, temp2) = (odd, even)
        stdout.write(str(temp1) + ' ' + str(temp2))
        stdout.write('\n')
