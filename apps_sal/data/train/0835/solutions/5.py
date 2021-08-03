t = input()
t = int(t)
while t > 0:
    n, m = input().split()

    if int(n) == 1 and int(m) == 2:
        print("Yes")
    elif int(n) == 2 and int(m) == 1:
        print("Yes")
    elif int(n) == 1 or int(m) == 1:
        print("No")
    elif int(n[-1]) % 2 == 0 or int(m[-1]) % 2 == 0:
        print("Yes")
    else:
        print("No")
    t = t - 1
