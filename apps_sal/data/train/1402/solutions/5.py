t = int(input())
for i in range(t):
    a1 = input()
    b1 = input()
    val1 = 0
    val2 = 0
    u = 0
    v = 0

    def gen(m):
        val1 = int(a1, 2)
        val2 = int(b1, 2)
        c = 0
        while m > 0:
            c += 1
            u = val1 ^ m
            v = val1 & m
            val1 = u
            m = 2 * v
        yield c
    val2 = int(b1, 2)
    g = gen(val2)
    for i in g:
        print(i)
