t = eval(input())
'''for i in range(t):
    s=input()
    print(s.count("4"))
'''

# second way is

for i in range(t):
    rem = []
    n = eval(input())
    while(n > 0):
        rem.append(n % 10)
        n = n // 10
    print(rem.count(4))
