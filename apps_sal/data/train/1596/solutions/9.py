def jumpsto(n):
    if n == 0:
        return 0
    elif n & n - 1 == 0:
        return 1
    jump = 0
    powe = 0
    n1 = n
    while n1 != 0:
        n1 = n1 // 2
        powe += 1
    powe -= 1
    jump += 1
    return jump + jumpsto(n - 2**powe)


for _ in range(int(input())):
    x, y = list(map(int, input().strip().split()))
    x += 1
    y += 1
    jumpx = jumpsto(x)
    jumpy = jumpsto(y)
    if jumpx == jumpy:
        print(0, 0)
    elif jumpx < jumpy:
        print(1, jumpy - jumpx)
    else:
        print(2, jumpx - jumpy)
