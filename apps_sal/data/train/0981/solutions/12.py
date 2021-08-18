MAX = 10000000000


def main():
    t = int(input())
    j = 0
    min = []
    while j < t:
        N = int(input())
        i = 0
        S = list(map(int, input().split()))
        S.sort()
        min.append(MAX)
        while i < N - 1:
            if S[i + 1] - S[i] < min[j]:
                min[j] = S[i + 1] - S[i]
            i = i + 1
        j = j + 1

    j = 0
    while j < t:
        print(min[j])
        j = j + 1


def __starting_point():
    main()


__starting_point()
