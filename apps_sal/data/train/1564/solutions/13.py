for _ in range(eval(input())):
    arr = [None] * 677
    inp = input()
    l = len(inp)
    for i in range(l - 1):
        a = inp[i]
        b = inp[i + 1]
        num = (ord(a) - 65) * 26 + (ord(b) - 65) + 1
        arr[num] = 1
    codes = 0
    for i in arr:
        if i == 1:
            codes += 1
    print(codes)
