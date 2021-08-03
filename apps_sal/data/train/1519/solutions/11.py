t = int(input())
for _ in range(t):
    n = int(input())
    st = bin(n)
    st = st[2:]
    # i=st.index("1")
    x = len(st)
    # print(2**n)
    if st.count("1") == 1:
        print(n)
    else:
        print(2**x)
