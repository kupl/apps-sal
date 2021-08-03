# cook your dish here
for u in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    d = 0
    c = 0
    x = s.count('b')
    for i in range(n):
        if(s[i] == 'b'):
            c += 1
        elif(s[i] == 'a'):
            d += (k * (k + 1) // 2) * x - (k * c)
    print(d)
