t = int(input())
while t > 0:
    n = int(input())
    s = input()
    arr = []
    for i in range(97, 113):
        arr.append(chr(i))
    i = 0
    while i < n:
        k = 0
        l = 15
        while k < l:
            m = (k + l) // 2
            if k >= l:
                break
            if s[i] == '0':
                l = m
            elif s[i] == '1':
                k = m + 1

            i = i + 1
        print(arr[k], end="")
    print()
    t = t - 1
