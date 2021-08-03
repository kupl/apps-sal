
for x in range(int(input())):
    l = int(input())
    s = input()
    z = 0
    for x in s:
        if x == '0':
            z += 1
    print(z * (l - z))
