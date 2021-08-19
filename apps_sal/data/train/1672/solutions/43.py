import math
arr = []
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

arr = arr[::-1]
for x in arr:
    if x >= 0:
        a = math.sqrt(abs(x))
        b = 5 * (abs(x)**3)
    else:
        a = math.sqrt(abs(x))
        b = -5 * (abs(x)**3)
    # print(x,a,b)
    fin = a + b
    fin = round(fin, 2)
    fin = str(fin)
    if str(fin[-3]) != ".":
        fin += "0"

    if float(fin) <= 400:
        print("f(" + str(x) + ") =", str(fin))
    else:
        print("f(" + str(x) + ") = MAGNA NIMIS!")
