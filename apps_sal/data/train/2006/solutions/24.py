n = int(input())
l = [int(i) for i in input().split()]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = 0
for i in l:
    g = gcd(g, i)
no_of_moves = max(l) // g - n
print('Alice' if no_of_moves & 1 else 'Bob')
