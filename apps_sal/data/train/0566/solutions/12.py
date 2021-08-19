# cook your dish here
t = int(input())
for z in range(t):
    a = input()
    b = input()
    s1 = set(a)
    s2 = set(b)
    if s1 & s2:
        print("Yes")
    else:
        print("No")
