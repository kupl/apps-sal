for _ in range(int(input())):
    k = int(input())
    ar = []
    for i in range(97, 123, 1):
        ar.append(chr(i))
    st = "".join(ar)
    an = ""
    while 1:
        an = st[k::-1] + an
        if k < 26:
            break
        k -= 25

    print(an)
