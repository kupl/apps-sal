def w(n):
    prime, p, a = [True for i in range(n + 1)], 2, []
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            a.append(p)
    return a


s, e, r = w(200), [], []
for i in range(len(s)):
    for j in range(len(s)):
        if(i != j):
            if (s[i] * s[j]) <= 200 and (s[i] * s[j]) not in e:
                e.append((s[i] * s[j]))
for i in range(len(e)):
    for j in range(len(e)):
        if (e[i] + e[j]) <= 200 and (e[i] + e[j]) not in r:
            r.append((e[i] + e[j]))
for _ in range(int(input())):
    print("YES") if (int(input())) in r else print("NO")
