t = int(input())
for _ in range(t):
    s = input()
    pref = [0] * len(s)
    if s[0] == '1':
        pref[0] += 1
    for i in range(1, len(s)):
        if s[i] == '1':
            pref[i] += 1
        pref[i] = pref[i] + pref[i - 1]
    k = 1
    cnt = 0
    while k + k * k <= len(s):
        r = k + k * k
        i = r - 1
        while i < len(s):
            if i - r >= 0:
                if pref[i] - pref[i - r] == k:
                    cnt += 1
                    i += 1
                else:
                    i += abs(k - (pref[i] - pref[i - r]))
            elif pref[i] == k:
                cnt += 1
                i += 1
            else:
                i += abs(k - pref[i])
        k += 1
    print(cnt)
