import math

seq = []
for _ in range(11):
    seq.append(int(input()))

for _ in range(11):
    n = seq.pop()
    aresult = math.sqrt(abs(n))
    bresult = (n ** 3) * 5
    result = aresult + bresult
    if result <= 400:
        print("f(%d) = %.2f" % (n, result))
    else:
        print("f(%d) = MAGNA NIMIS!" % n)
