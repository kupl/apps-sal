it = list(map(int, input().split()))
(n, m) = it[:2]
(w, b) = it[2:4]
aa = it[4:4 + 2 * w]
aa = [[aa[i * 2], aa[i * 2 + 1]] for i in range(w)]
bb = it[4 + 2 * w:]
bb = [[bb[i * 2], bb[i * 2 + 1]] for i in range(b)]
ss = [[] for i in range(n)]
for i in aa:
    ss[i[0] - 1].append([i[1] - 1, 1])
for i in bb:
    ss[i[0] - 1].append([i[1] - 1, 0])
ss = [sorted(i) for i in ss]
tot = 0
for j in range(n):
    ind = 0
    co = 0
    st = []
    for i in ss[j]:
        if i[1] == 1:
            co += 1
            if co <= 1:
                st.append(i)
                continue
            a = i[0] - ind + 1
            b = 1 + 1
            for ii in st:
                a = ind
                b = ii[0] - 1
                a = i[0] - a + 1
                b = i[0] - b + 1
                su = (a + b) * (a - b + 1) // 2
                tot += su
                ind = ii[0] + 1
            st = [i[:]]
        else:
            co = 0
            a = i[0] - ind + 1
            b = 1 + 1
            su = (a + b) * (a - b + 1) // 2
            tot += su
            ind = i[0] + 1
            for ii in st:
                tot -= i[0] - ii[0] + 1
            st = []
    a = ind
    b = m - 1
    if a <= b:
        a = m - a
        b = m - b
        su = (a + b) * (a - b + 1) // 2
        tot += su
    for ii in st:
        tot -= m - ii[0]
print(tot)
