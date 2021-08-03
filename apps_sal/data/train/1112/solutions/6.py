def func(num):
    count = 1
    for i in range(1, num + 1):
        for j in range(1, num + 2 - i):
            print(count, end='')
            count += 1
        print()


for _ in range(int(input())):
    num = int(input())
    func(num)
