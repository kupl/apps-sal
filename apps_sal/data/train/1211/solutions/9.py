def Solve4():
    a = input()
    x = len(a)
    while "abc" in a:
        for i in range(x - 3):
            if a[i:i + 3] == 'abc':
                a = a[:i] + a[i + 3:]
                break
    print(a)


for _ in range(int(input())):
    Solve4()
