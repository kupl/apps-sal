import string

t = 0
try:
    t = int(input().strip())
except:
    pass
for _ in range(0, t):
    r, c = [int(j) for j in input().split()]
    a = []
    flag = False
    m = ""
    for q in range(0, r):
        ll = input().lower()
        a.append(ll)
        m = m + ll

    for q in a:
        if q.find("spoon") != -1:
            flag = True
            break
    if not flag:
        q = 0
        bb = (r - 4) * c
        while q < bb:
            if m[q] == "s":
                ja = m[q] + m[q + c] + m[q + 2 * c] + m[q + 3 * c] + m[q + 4 * c]
                if ja == "spoon":
                    flag = True
                    break
            q += 1
    if flag:
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
