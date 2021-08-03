import math

seq = []

for next in range(11):
    seq.append(int(input()))

for next in range(11):
    var = seq.pop()
    aresult = math.sqrt(abs(var))
    bresult = (var**3) * 5
    result = aresult + bresult

    if 400 >= result:
        print("f(%d) = %.2f" % (var, result))
    else:
        print("f(%d) = MAGNA NIMIS!" % var)
