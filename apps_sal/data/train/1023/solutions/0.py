for _ in range(int(input())):
    n = int(input())
    count = 1
    l = 3 * (n - 1)
    i = 0
    if n == 1:
        print(1)
        continue
    while count <= l - n:
        for j in range(i + 1):
            if j == i:
                print(count)
                count += 1
            elif j == 0:
                print(count, end='')
                count += 1
            else:
                print(' ', end='')
        i += 1
    while count <= l:
        print(count, end='')
        count += 1
    print()
