# cook your dish here
for i in range(int(input())):
    n, orgin = map(str, input().split())
    l = 0
    for i in range(int(n)):
        a = list(input().split())

        if len(a) == 2:
            if "CONTEST_WON" == a[0]:
                l += 300
                k = int(a[1])
                if k < 20:
                    l = 20 - k + l
            elif a[0] == "BUG_FOUND":
                l += int(a[1])
        else:
            if "TOP_CONTRIBUTOR" == a[0]:
                l += 300
            elif a[0] == "CONTEST_HOSTED":
                l += 50

    if orgin == "INDIAN":
        print(l // 200)
    elif orgin == "NON_INDIAN":
        print(l // 400)
