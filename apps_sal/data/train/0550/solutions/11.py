try:

    def dectobin(a):
        r = [int(i) for i in bin(a)[2:]]
        return r

    def bintodec(a):
        r = int(''.join((str(x) for x in a)), 2)
        return r

    def s(a):
        a = [a[-1]] + a[:-1]
        return a
    for i in range(int(input())):
        (a, b) = map(int, input().split())
        bina = dectobin(a)
        binb = dectobin(b)
        ans = []
        ans.append(a ^ b)
        bits = len(bina) - len(binb)
        if bits < 0:
            for j in range(bits):
                bina.insert(0, 0)
        elif bits > 0:
            for j in range(bits):
                binb.insert(0, 0)
        for j in range(len(binb)):
            binb = s(binb)
            b = bintodec(binb)
            ans.append(a ^ b)
        print(ans.index(max(ans)), max(ans))
except:
    pass
