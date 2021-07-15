from math import sqrt
arr = [0 for _ in range(11)]
for i in range(11):
    arr[10-i] = int(input())
for i in arr:
    tmp = sqrt(abs(i)) + (i**3)*5
    if tmp >= 400:
        print("f({}) = MAGNA NIMIS!".format(i))
    else:
        print("f({}) = {:.2f}".format(i,round(tmp,2)))
