for _ in range(int(input())):
    ip = list(map(int, input().split()))
    n = ip[0]
    k = ip[1]
    l = list(map(int, input().split()))
    d = {}
    i = 0
    start = 0
    end = 0
    j = 0
    m = 0
    while j < n:
        d.setdefault(l[j], 0)
        d[l[j]] += 1
        if(len(d) >= k):
            start = i
            end = j
            if d[l[i]] > 1:
                d[l[i]] -= 1
            else:
                d.pop(l[i])
            if d[l[j]] > 1:
                d[l[j]] -= 1
            else:
                d.pop(l[j])
            j -= 1
            i += 1
        start = i
        end = j + 1
        if m <= end - start:
            m = end - start
        j += 1

    print(m)
