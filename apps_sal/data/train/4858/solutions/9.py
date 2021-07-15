def johnann(n, jnota):
    j, a = [0], [1]
    for i in range(1,n):
        j.append(i-a[j[-1]])
        a.append(i-j[a[-1]])
    return j if jnota else a

john = lambda n: johnann(n, True)
ann = lambda n: johnann(n, False)
sum_john = lambda n: sum(john(n))
sum_ann = lambda n: sum(ann(n))

