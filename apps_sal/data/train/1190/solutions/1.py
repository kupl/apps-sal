n = int(input())
for i in range(n):
    p = int(input())
    menu = 0
    if p > 2048:
        menu = p // 2048 - 1
        p = p - 2048 * menu
    while p != 0:
        if p % 2 != 0:
            menu = menu + 1
        p = p // 2
    print(menu)
