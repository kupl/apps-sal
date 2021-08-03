from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    s = input()
    n = int(s)
    n1 = n
    l = list(s)
    s1 = 0
    while n1 != 0:
        s1 += n1 % 10
        n1 //= 10
    if n % s1 == 0:
        print("Yes")
    else:
        print("No")
