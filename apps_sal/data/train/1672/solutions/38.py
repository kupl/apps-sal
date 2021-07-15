from math import sqrt
f = lambda x: sqrt(abs(x))
g = lambda x: x**3*5
arr = []
for _ in range(11):
    arr.append(int(input()))
arr.reverse()
for e in arr:
    r = f(e)+g(e)
    if 400 < r:
        print("f(%d) = " % (e) + "MAGNA NIMIS!")
        continue
    print("f(%d) = %.2f" % (e, r))
