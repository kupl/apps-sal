for i in range(int(input())):
    n = int(input())
    val = 0
    for i in range(1, n + 1):
        st = ''
        temp = val + i
        val = temp
        for j in range(i):
            print(temp, end='')
            temp -= 1
        print()
