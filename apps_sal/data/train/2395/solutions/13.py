tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    a = b = '1'
    flag = None
    for i in s[1:]:
        if int(i) % 2 == 0 and not flag:
            num = int(i) // 2
            a += str(num)
            b += str(num)
        else:
            num = int(i) // 2
            if not flag:
                a += str(num + 1)
                b += str(num)
                flag = True
            else:
                a += str(0)
                b += str(i)
    print(a, b, sep="\n")

