def process(N):
    if not '4' in N:
        return '4' * (len(N) + 1)
    i = N.rindex('4')
    return N[:i] + '7' + '4' * len(N[i + 1:])


def main():
    T = int(input().strip())
    for t in range(T):
        N = input().strip()
        print(process(N))


main()
