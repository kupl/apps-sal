t = eval(input())
'for i in range(t):\n    s=input()\n    print(s.count("4"))\n'
for i in range(t):
    rem = []
    n = eval(input())
    while n > 0:
        rem.append(n % 10)
        n = n // 10
    print(rem.count(4))
