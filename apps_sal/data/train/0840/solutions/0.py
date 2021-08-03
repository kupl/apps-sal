def func(num):
    for i in range(num):
        if i < num // 2 + 1:
            print(' ' * i, end='')
            print('*')
        else:
            print(' ' * (num - i - 1), end='')
            print('*')


for _ in range(int(input())):
    num = int(input())
    func(num)
