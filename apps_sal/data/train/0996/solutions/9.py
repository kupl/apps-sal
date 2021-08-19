(val, A, B) = (0, 0, 0)
for a in range(int(input())):
    (c, d) = input().split()
    A += int(c)
    B += int(d)
    b = abs(A - B)
    if b > val:
        val = b
        if int(c) > int(d):
            w = 1
        else:
            w = 2
print(w, val)
