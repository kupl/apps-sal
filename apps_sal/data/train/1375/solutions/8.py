from sys import stdin

T = int(stdin.readline().strip())
for x in range(T):
    N = stdin.readline().strip()
    N = N[::-1]
    while True:
        if N[0] == 0:
            N = N[1:]
        else:
            break
    print(int(N))
