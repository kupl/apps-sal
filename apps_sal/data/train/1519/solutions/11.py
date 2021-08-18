t = int(input())
for _ in range(t):
    n = int(input())
    st = bin(n)
    st = st[2:]
    x = len(st)
    if st.count("1") == 1:
        print(n)
    else:
        print(2**x)
