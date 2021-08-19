T = int(input())
while T:
    l = input()
    n = len(l)
    if n >= 10:
        print(10)
    else:
        print(n)
    T -= 1
