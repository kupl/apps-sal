t = int(input())
while t:
    (w, k) = input().split()
    k = int(k)
    char = {}
    for c in w:
        if c not in char.keys():
            char[c] = 1
        else:
            char[c] += 1
    counts = list(char.values())
    counts.sort()
    l = len(counts)
    ans = len(w) + 1
    for i in range(l):
        temp = 0
        for j in range(l):
            if counts[j] < counts[i]:
                temp += counts[j]
            elif counts[j] > counts[i] + k:
                temp += counts[j] - counts[i] - k
        ans = min(ans, temp)
    print(ans)
    t -= 1
