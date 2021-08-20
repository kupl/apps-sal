(n, q) = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        ind = s[1] - 1
        jump = s[2]
        j = ind + 1
        val = l[ind]
        while True:
            if j >= len(l):
                break
            if l[j] > val and j - ind <= 100 and (jump > 0):
                val = l[j]
                jump -= 1
                ind = j
            if j - ind > 100:
                break
            if jump <= 0:
                break
            j += 1
        print(ind + 1)
    else:
        left = s[1] - 1
        r = s[2]
        x = s[3]
        for i in range(left, r):
            l[i] += x
