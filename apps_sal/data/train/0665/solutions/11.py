for _ in range(int(input())):
    (n, m) = map(int, input().split())
    scores = list(map(int, input().split()))
    usr_mnthly = {}
    usr_ranks = {}
    for i in range(n):
        scrs = list(map(int, input().split()))
        usr_mnthly[i] = [scores[i]]
        usr_ranks[i] = []
        for j in scrs:
            usr_mnthly[i].append(usr_mnthly[i][-1] + j)
    for mnth in range(1, m + 1):
        mnthly = {i: usr_mnthly[i][mnth] for i in range(n)}
        mnthly = sorted(mnthly.items(), key=lambda x: x[1], reverse=True)
        prev = -9999999999
        rank = 0
        pos = 1
        for (key, value) in mnthly:
            if value == prev:
                usr_ranks[key].append(rank)
                pos += 1
            else:
                rank += pos
                usr_ranks[key].append(rank)
                pos = 1
            prev = value
    ans = 0
    for i in range(n):
        mnths = usr_mnthly[i][1:]
        ranks = usr_ranks[i]
        if ranks.index(min(ranks)) != mnths.index(max(mnths)):
            ans += 1
    print(ans)
