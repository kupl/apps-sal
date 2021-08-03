t = int(input())
for i in range(t):
    a1 = input()
    b1 = input()
    val1 = 0
    val2 = 0
    c = 0
    u = 0
    v = 0
    val1 = int(a1, 2)
    val2 = int(b1, 2)
    while(val2 > 0):
        c += 1
        u = val1 ^ val2
        v = val1 & val2
        val1 = u
        val2 = 2 * v
    print(c)
