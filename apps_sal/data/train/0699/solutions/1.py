r = int(input())
while r > 0:
    (n, k, d) = map(int, input().split())
    l = list(map(int, input().split()))[0:n]
    sum = 0
    for x in range(n):
        sum = sum + l[x]
    c = sum // k
    if c >= d:
        print(d)
    else:
        print(c)
    r -= 1
'""\n5\n1 5 31\n4\n1 10 3\n23\n2 5 7\n20 36\n2 5 10\n19 2\n3 3 300\n1 1 1\n'
