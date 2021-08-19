__author__ = 'Deepak'
t = eval(input())
while t > 0:
    t -= 1
    a = eval(input())
    k = 0
    while a - k >= 0:
        a -= k
        k += 1
    print(k - 1)
