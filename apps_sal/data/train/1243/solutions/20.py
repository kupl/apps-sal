def func(num):
    for x in num:
        if x == '0' or x == '5':
            print(1)
            return
    print(0)


for _ in range(int(input())):
    num = input()
    func(num)
