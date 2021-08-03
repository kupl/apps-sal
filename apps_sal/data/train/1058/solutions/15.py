# cook your dish here
t = int(input())
while t:
    n = int(input())
    l = []
    while n > 0:
        temp = n % 10
        n //= 10

        l.append(temp)
    for i in range(len(l)):
        l[i] -= 2
    s = ""
    l.reverse()
    for i in l:
        s += str(i)
    print(s)
    t -= 1
