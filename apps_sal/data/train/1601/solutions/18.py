from sys import stdin, stdout
l_in = stdin.readline
l_out = stdout.write
t = int(l_in())
for i in range(t):
    MaxM = 0
    count = 0
    (N, P) = list(map(int, l_in().strip().split()))
    ar = list(range(1, P + 1))
    for i in ar:
        for j in ar:
            for k in ar:
                M = N % i % j % k % N
                if M > MaxM:
                    count = 1
                    MaxM = M
                elif M == MaxM:
                    count = count + 1
    print(count)
