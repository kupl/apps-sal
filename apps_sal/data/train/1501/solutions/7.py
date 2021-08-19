mod = 1000000007
n, q = map(int, input().split())
pot = pow(2, n, mod)  # 2 to the power n and then mod mod
e = ((pot - 1) * 2) % mod
right = n + 1
left = n + 1
top = 1
bottom = pot
for _ in range(q):
    l = input()
    add = 0
    if l[0] == '1':
        if l[2] == '1':
            add = right
            top *= 2
            bottom *= 2
        elif l[2] == '2':
            add = left
            top *= 2
            bottom *= 2
        elif l[2] == '3':
            add = top
            right *= 2
            left *= 2
            top = bottom
        else:
            add = bottom
            left *= 2
            right *= 2
            bottom = top
        e = (e * 2 + add) % mod
    else:
        print(e)
