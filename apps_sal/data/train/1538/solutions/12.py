from sys import stdin, stdout


def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


for _ in range(int(stdin.readline())):
    (A, B) = list(map(int, stdin.readline().split()))
    g = gcd(A, B)
    l = A // g * B
    stdout.write(str(g) + ' ')
    stdout.write(str(l) + '\n')
