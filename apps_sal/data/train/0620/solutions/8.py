for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    l = [int(i) for i in input().split()]
    maxi = 0
    grtr = 0
    st = 0
    from collections import defaultdict
    big = defaultdict(int)
    for end in range(n):
        if l[end] > k:
            big[l[end]] += 1
            if big[l[end]] == 1:
                grtr += 1
        while grtr > 1:
            if l[st] > k:
                big[l[st]] -= 1
                if big[l[st]] <= 0:
                    grtr -= 1
            st += 1
        maxi = max(maxi, end - st + 1)
    print(maxi)
