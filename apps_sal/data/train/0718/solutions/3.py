def func(num):
    no_terms = num * (num + 1) // 2
    lst = [0, 1]
    for i in range(2, no_terms):
        lst.append(lst[i - 1] + lst[i - 2])
    k = 0
    for i in range(1, num + 1):
        for j in range(i):
            print(lst[k], ' ', end='')
            k += 1
        print()


for _ in range(int(input())):
    num = int(input())
    func(num)
