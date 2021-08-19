for _ in range(int(input())):
    s = input()
    a = ''
    for i in s:
        a = a + str(int(i) - 2)
    print(a)
