x = []
for i in range(11):
    x.append(int(input()))
x = x[::-1]
for i in range(11):
    a = x[i]
    b = x[i]
    a = (abs(a))**0.5
    b = b ** 3 * 5
    if a + b > 400:
        print(f"f({x[i]}) = MAGNA NIMIS!")
    else:
        print(f"f({x[i]}) = ", end='')
        print("{:.2f}".format(round(a + b, 2)))
