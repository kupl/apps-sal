try:
    T = int(input())
    while T > 0:
        N = int(input())
        midway = (N // 2) - 1
        num = list(map(int, input().split()[:N]))
        max_beg = max(num)
        first_occr = num.index(max_beg)
        num.reverse()
        last_occr = num.index(max_beg)
        last_occr = N - 1 - last_occr

        if last_occr - first_occr >= midway:
            print(0)
        else:
            if first_occr == last_occr:
                first_occr = midway
                print(N - 1 - first_occr)
            else:
                gap = last_occr - first_occr
                first_occr = midway
                last_occr = first_occr + gap
                print(N - 1 - last_occr)
        T -= 1

except EOFError as e:
    print("")
