mod = 10**9 + 7
for i in range(int(input())):
    n, k, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = [0 for i in range(k + 1)]
    ans[0] = 1
    curr_ending = 1
    for i in range(n):
        mod_a = a[i] % m
        start = curr_ending - (curr_ending % m - mod_a) % m
        if(mod_a == curr_ending % m and curr_ending < k):
            curr_ending += 1
        for i in range(start, 0, -m):
            ans[i] += ans[i - 1]
            if(ans[i] > mod):
                ans[i] = ans[i] - mod
    print(ans[k])
