for t in range(0, int(input())):
    n = int(input())
    ss = list(map(str, input().split()))

    unique_words = set(ss)

    ans = ""
    cnt = 0

    for i in unique_words:
        x = ss.count(i)
        if x > cnt:
            cnt = x
            ans = i
        elif x == cnt:
            if i < ans:
                ans = i

    print(ans)
