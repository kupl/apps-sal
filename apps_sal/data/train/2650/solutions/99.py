
def __starting_point():
    N, L = list(map(int, input().split()))
    si = []
    for i in range(N):
        si.append(str(input()))
    si.sort()
    print((''.join(si)))


__starting_point()
