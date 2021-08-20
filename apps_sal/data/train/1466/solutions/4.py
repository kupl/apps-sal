(n, q) = list([int(x) for x in input().split()])
a = list([int(x) for x in input().split()])
xor_a = 0
for i in a:
    xor_a = xor_a ^ i
a.append(xor_a)
prefix = [a[0]]
for i in range(1, len(a)):
    prefix.append(a[i] ^ prefix[i - 1])
for i in range(0, q):
    x = int(input())
    print(prefix[(x - 1) % (n + 1)])
