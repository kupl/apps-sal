T = int(input())
II = 0
while II < T:
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    if a < b:
        a, b = b, a
    print(max(2 * b, a)**2)
    II += 1
