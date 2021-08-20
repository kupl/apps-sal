t = int(input())
for _ in range(t):
    st = input()
    s = set(st)
    a = []
    f1 = f2 = 0
    for i in s:
        a.append(st.count(i))
    a.sort()
    if len(a) >= 3:
        for i in range(2, len(a)):
            if a[i] != a[i - 1] + a[i - 2]:
                f1 = 1
                break
        x = a[0]
        a[0] = a[1]
        a[1] = x
        for i in range(2, len(a)):
            if a[i] != a[i - 1] + a[i - 2]:
                f2 = 1
                break
        if f1 == 1 and f2 == 1:
            print('Not')
        else:
            print('Dynamic')
    else:
        print('Dynamic')
