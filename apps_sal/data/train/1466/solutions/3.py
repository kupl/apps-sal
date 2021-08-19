# cook your dish here
n, q = list(map(int, input().split(' ')))
ar, xor = list(map(int, input().split(' '))), 0

for x in ar:
    xor ^= x
ar.append(xor)

prefix = [0] * (n + 1)
prefix[0] = ar[0]

for i in range(1, len(prefix)):
    prefix[i] = ar[i] ^ prefix[i - 1]
for i in range(q):
    print(prefix[(int(input()) - 1) % (n + 1)])
