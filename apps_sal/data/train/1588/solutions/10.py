t = int(input())
while t:
    re = []
    st = {}
    m = {}
    for _ in range(int(input())):
        (a, b) = input().split()
        b = int(b)
        if b in list(st.keys()):
            st[b] += 1
        else:
            st[b] = 1
            m[b] = a
        re.append(int(b))
    count = 0
    re = list(set(re))
    re.sort()
    ind = 0
    for i in re:
        if st[i] == 1:
            count += 1
            ind = i
            break
    if count == 1:
        print(m[ind])
    else:
        print('Nobody wins.')
    t -= 1
