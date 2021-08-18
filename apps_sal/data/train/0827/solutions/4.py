for _ in range(int(input())):
    n, k = map(int, input().split())
    st = input()
    a = st.count('a')
    b = st.count('b')
    c = 0
    ca = 0
    for i in range(n):
        if st[i] == 'a':
            ca += 1
        if st[i] == 'b':
            c += ca

    print(a * b * (k * (k - 1) // 2) + c * k)
