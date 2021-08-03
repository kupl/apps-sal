# cook your dish here
t = int(input())
while t > 0:
    s = input()
    n = len(s)
    x = s.count('1')
    if n % 2 == 1 or x == 0 or x == n:
        print(-1)
    else:
        print(abs(n // 2 - x))
    t -= 1
