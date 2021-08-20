for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        for j in range(count):
            print(' ', end='')
        print('*')
        if i < n // 2:
            count += 1
        else:
            count -= 1
