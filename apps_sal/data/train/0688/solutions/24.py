T = int(input())
for _ in range(T):
    a = input()
    c = 0
    i = 1
    curr = a[0]
    while(i < 8):
        if a[i] != curr:
            curr = a[i]
            c = c + 1
        i = i + 1
    if a[0] != a[7]:
        c = c + 1
    if c <= 2:
        print("uniform")
    else:
        print("non-uniform")
