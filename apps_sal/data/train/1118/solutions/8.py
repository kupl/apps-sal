t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    bits = input().strip()
    check1 = ''
    check2 = ''
    c1 = 0
    for _ in range(n):
        check1 = check1 + str(c1)
        check2 = check2 + str((c1 + 1) % 2)
        c1 = (c1 + 1) % 2
    no1 = 0
    no2 = 0
    for i in range(n):
        no1 = no1 + (1 if not bits[i] == check1[i] else 0)
        no2 = no2 + (1 if not bits[i] == check2[i] else 0)
    print(min(no1, no2))
